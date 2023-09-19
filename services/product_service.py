from fastapi import HTTPException
from models.product_model import Product
from schemas.product_schema import ProductInput
from sqlalchemy.orm import Session
#GET
# skip and limit for pagination
def get_all_products(db: Session, skip: int =0, limit: int =0, cat_id: int =0) -> list[Product]:
    if cat_id ==0:
        return db.query(Product).offset(skip).limit(limit).all()
    else:
        return db.query(Product).filter(Product.category_id==cat_id).offset(skip).limit(limit)
#POST
def create_product(db: Session, product: ProductInput) -> Product:
    # serialize category input as dict, and then use ** to unpack dict to use as params.
    new_product = Product(**(product.model_dump()))
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

#GET{id}
def get_product_by_id(db: Session, id: int) -> Product:
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id: {id} is not found")
    return product


#PUT{id}
def put_product(db:Session, id: int, new_product: Product) -> Product:
    product = db.query(Product).filter(Product.id==id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id: {id} is not found")
    else:
        for key, value in new_product.dict().items():
            setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product