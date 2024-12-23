from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Item, User
from schemas import ItemCreate, ItemResponse, UserCreate, UserResponse
from crud import get_items, get_item, create_item, delete_item, create_user

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/items/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=ItemResponse)
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@app.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/register/user", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)