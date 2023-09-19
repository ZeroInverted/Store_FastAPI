from pydantic import BaseModel
class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    img_url: str
    category_id: int

class ProductInput(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True