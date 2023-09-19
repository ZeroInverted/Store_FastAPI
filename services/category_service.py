from models.category_model import Category
from schemas.category_schema import CategoryInput
from sqlalchemy.orm import Session

# skip and limit for pagination
def get_all_categories(db: Session, skip: int =0, limit: int =0) -> list[Category]:
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryInput) -> Category:
    # serialize category input as dict, and then use ** to unpack dict to use as params.
    new_category = Category(**(category.model_dump()))
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category