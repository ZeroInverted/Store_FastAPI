from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__="categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True) 
    
    products = relationship("Product", back_populates="category")
    