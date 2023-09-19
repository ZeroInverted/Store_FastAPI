from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryInput(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True