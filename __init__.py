# Database initialization, run only once to create tables, this solution dodges the problem fo circular import

from .database import Base, engine
from .models.category_model import Category
from .models.product_model import Product

Base.metadata.create_all(engine)