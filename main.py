from fastapi import FastAPI
from routers.category_router import category_router

store = FastAPI()

store.include_router(category_router, prefix="/categories")

