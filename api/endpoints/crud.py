from api.schemas import ProductCreate
from db.models import Product, Category

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload


async def get_or_create_category(
        db: AsyncSession,
        category_name: str
) -> Category:
    """Получить или создать категорию"""
    result = await db.execute(
        select(Category)
        .where(Category.name == category_name)
    )
    category = result.scalar_one_or_none()
    if category is None:
        category = Category(name=category_name)
        db.add(category)
        await db.commit()
        await db.refresh(category)
    return category


async def create_product(
        db: AsyncSession,
        product: ProductCreate
):
    """Создать товар"""
    category = await get_or_create_category(db, product.category_name)

    db_product = Product(
        title=product.title,
        description=product.description,
        price=product.price,
        size=product.size,
        category_id=category.id
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    await db.refresh(db_product, ["category"])
    return db_product


async def get_product(
        db: AsyncSession,
        product_id: int
) -> Product:
    """Получить товар по ID"""
    result = await db.execute(
        select(Product)
        .options(selectinload(Product.category))
        .filter(Product.id == product_id)
    )
    product = result.scalar_one_or_none()
    return product


async def get_all_products(
        db: AsyncSession,
        title: str = None,
        category_name: str = None
) -> List[dict]:
    """Получить все товары"""
    query = (
        select(Product, Category.name.label("category_name"))
        .join(Product.category)
    )

    if title:
        lower_title = title.lower()
        query = query.filter(func.lower(Product.title).ilike(f"%{lower_title}%"))
    if category_name:
        lower_category_name = category_name.lower()
        query = query.filter(func.lower(Category.name) == category_name)

    result = await db.execute(query)
    return [
        {
            "id": product.id,
            "title": product.title,
            "description": product.description,
            "price": float(product.price),
            "size": float(product.size) if product.size is not None else None,
            "category_name": category_name
        }
        for product, category_name in result.all()
    ]

async def delete_product_by_id(
        product_id: int,
        db: AsyncSession
):
    """Удалить товар по ID"""
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    await db.delete(product)
    await db.commit()
    return True
