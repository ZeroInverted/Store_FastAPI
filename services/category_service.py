from models.category_model import Category
from schemas.category_schema import CategoryInput
from schemas.response_schema import Category_API_Response
from sqlalchemy.orm import Session


# skip and limit for pagination
def get_all_categories(db: Session, skip: int =0, limit: int =0) -> Category_API_Response:
    categories = db.query(Category).offset(skip).limit(limit).all()
    if categories is not None:
        return Category_API_Response(success=True, results=categories)
    else:
        error = ["No categories found. Please add a category first."]
        return Category_API_Response(success=False, messages=error, status_code=404)

def create_category(db: Session, category: CategoryInput) -> Category_API_Response:
    # serialize category input as dict, and then use ** to unpack dict to use as params.
    new_category = Category(**(category.model_dump()))
    try:
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return Category_API_Response(success=True, results=new_category)
    except:
        error = ["An error occurred while attempting to create a category"]
        return Category_API_Response(success=False, messages=error, status_code=409)