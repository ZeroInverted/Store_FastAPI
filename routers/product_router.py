from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.product_service import get_all_products, get_product_by_id, put_product, create_product
from schemas.product_schema import ProductInput, Product
product_router = APIRouter()

@product_router.get("/", response_model=list[Product])
def get_products(skip: int = 0, limit: int = 10, cat_id: int = 0, db: Session = Depends(get_db)):
    return get_all_products(db, skip, limit, cat_id)

@product_router.get("/{id}", response_model=Product)
def get_specific_product(id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, id)
    
@product_router.post("/", response_model=Product)
def post_product(product: ProductInput, db: Session = Depends(get_db)):
    return create_product(db, product)

@product_router.put("/{id}", response_model=Product)
def update_specific_product(id: int, product: ProductInput, db: Session = Depends(get_db)):
    return put_product(db, id, product)
