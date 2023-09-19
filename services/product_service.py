from fastapi import HTTPException
from models.product_model import Product
from schemas.product_schema import ProductInput
from schemas.response_schema import Product_API_Response
from sqlalchemy.orm import Session
#GET
# skip and limit for pagination
def get_all_products(db: Session, skip: int =0, limit: int =0, cat_id: int =0) -> Product_API_Response:
    if cat_id ==0:
        products = db.query(Product).offset(skip).limit(limit).all()
        if products is not None:    
            return Product_API_Response(success=True, results=products)
        else:
            error=["No products with such a category id."]
            return Product_API_Response(success=False, messages=error, status_code=404)
    else:
        products =  db.query(Product).filter(Product.category_id==cat_id).offset(skip).limit(limit)
        if products is not None:    
            return Product_API_Response(success=True, results=products)
        else:
            error=["No products found."]
            return Product_API_Response(success=False, messages=error, status_code=404)
#POST
def create_product(db: Session, product: ProductInput) -> Product_API_Response:
    # serialize category input as dict, and then use ** to unpack dict to use as params.
    new_product = Product(**(product.model_dump()))
    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return Product_API_Response(success=True, results=new_product)
    except Exception as e:
        print(e.format())
        error=["Error creating product"]
        return Product_API_Response(success=False, messages=error, status_code=409)

#GET{id}
def get_product_by_id(db: Session, id: int) -> Product_API_Response:
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        error = [f"Product with id: {id} is not found"]
        return Product_API_Response(success=False, messages=error)
    else:
        return Product_API_Response(success=True, results=product)


#PUT{id}
def put_product(db:Session, id: int, new_product: Product) -> Product_API_Response:
    product = db.query(Product).filter(Product.id==id).first()
    if product is None:
        error = [f"Product with id: {id} is not found"]
        return APIResponse(success=False, messages=error, status_code=404)
    else:
        for key, value in new_product.dict().items():
            setattr(product, key, value)
    try:
        db.commit()
        db.refresh(product)
        return APIResponse(success=True, results=product)
    except:
        error=[f"Error updating resource of id: {id}"]
        return APIResponse(success=False, messages=error, status_code=409)