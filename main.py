from fastapi import FastAPI
from routers.category_router import category_router
from routers.product_router import product_router
from fastapi.middleware.cors import CORSMiddleware
store = FastAPI()

store.include_router(category_router, prefix="/categories")
store.include_router(product_router, prefix="/products")

origins = ["*"]

store.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
