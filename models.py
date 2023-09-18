from sqlalchemy import Column, Integer,Float, String, ForeignKey 
from sqlalchemy.orm import relationship
from database import base

class Product(base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    img_url = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

class Category(base):
    __table__="categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True) 
    
    products = relationship("Product", back_populates="category")