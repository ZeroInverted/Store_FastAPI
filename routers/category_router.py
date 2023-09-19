from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.category_service import get_all_categories, create_category
from schemas.category_schema import CategoryInput
category_router = APIRouter()

@category_router.get("/")
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    get_all_categories(db, skip, limit)
    
@category_router.post("/")
def post_category(category: CategoryInput, db: Session = Depends(get_db)):
    create_category(db, category)
