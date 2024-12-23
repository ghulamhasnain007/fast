# from fastapi import FastAPI;
# from app.routes.todo_routes import router as todo_router
# app = FastAPI()

# # @app.get("/")
# # def read_root():
# #     return {"message": "Welcome to FastAPI Todo App"}


# app.include_router(todo_router)


# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.dependencies import get_db
from app.models.user_model import Product

app = FastAPI()

# Pydantic schema for input validation
class ProductCreate(BaseModel):
    name: str
    price: int
    description: str

@app.post("/products/create")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, price=product.price, description=product.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products/")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()

@app.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
