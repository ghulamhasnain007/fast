from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from sqlalchemy.orm import relationship
from app.database import Base



# Define a Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)  # Auto-increment ID
    name = Column(String, nullable=False)  # Product name
    price = Column(Float, nullable=False)  # Price of the product
    description = Column(String, nullable=True)  # Optional description
    # category_id = Column(Integer, ForeignKey("categories.id"))  # Foreign key to the Category table

    # # Relationship with the Category table
    # category = relationship("Category", back_populates="products")




# Define a Category model
# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)  # Auto-increment ID
#     name = Column(String, unique=True, nullable=False)  # Unique category name
#     description = Column(String, nullable=True)  # Optional description

#     # Relationship with the Product table
#     products = relationship("Product", back_populates="category")
