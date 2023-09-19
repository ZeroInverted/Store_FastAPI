from pydantic import BaseModel
from .category_schema import Category
from .product_schema import Product

class Category_API_Response(BaseModel):
    success: bool
    results: list[Category] | Category | None = None
    messages: list[str] | None = None
    status_code: int = 200

class Product_API_Response(BaseModel):
    success: bool
    results: list[Product] | Product | None = None
    messages: list[str] | None = None
    status_code: int = 200