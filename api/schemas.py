from pydantic import BaseModel


#--------------------------Валидация категорий--------------------------
class CategoryBase(BaseModel):
    name: str


class CategoryResponse(CategoryBase):
    id: int
    class Config:
        from_attributes = True


#--------------------------Валидация товаров--------------------------
class ProductCreate(BaseModel):
    title: str
    description: str | None = None
    price: float
    size: float | None = None
    category_name: str


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
