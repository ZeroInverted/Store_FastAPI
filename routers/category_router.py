from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.category_service import get_all_categories, create_category
from schemas.category_schema import CategoryInput, Category
from schemas.response_schema import Category_API_Response
category_router = APIRouter()

@category_router.get("/", response_model=Category_API_Response)
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_categories(db, skip, limit)
    
@category_router.post("/", response_model=Category_API_Response)
def post_category(category: CategoryInput, db: Session = Depends(get_db)):
    return create_category(db, category)
