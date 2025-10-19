from fastapi import APIRouter, Depends, HTTPException
from api.schemas import ProductResponse, ProductCreate
from api.endpoints.crud import create_product, get_product, get_all_products, delete_product_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from api.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/products", response_model=ProductResponse)
async def create_new_product(
        product: ProductCreate,
        db: AsyncSession = Depends(get_db)
):
    try:
        db_product = await create_product(db, product)

        return ProductResponse(
            id=db_product.id,
            title=db_product.title,
            description=db_product.description,
            price=db_product.price,
            size=db_product.size,
            category_name=db_product.category.name
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product_by_id(
        product_id: int,
        db: AsyncSession = Depends(get_db),
):
    try:
        product = await get_product(db, product_id)

        return ProductResponse(
            id=product.id,
            title=product.title,
            description=product.description,
            price=product.price,
            size=product.size,
            category_name=product.category.name
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"Товар c {product_id} не найден"
        )


@router.get("/products", response_model=List[ProductResponse])
async def get_products(
        title: str = None,
        category_name: str = None,
        db: AsyncSession = Depends(get_db)
):
    try:
        return await get_all_products(db, title, category_name)
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail="Товаров не обнаружено"
        )


@router.delete("/products/{product_id}")
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await delete_product_by_id(product_id, db)
        if result:
            return {
                "status": "Success",
                "detail": f"Товар с ID <{product_id}> удален"
            }
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"Товар c {product_id} не найден"
        )
