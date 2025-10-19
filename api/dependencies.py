from db.async_session import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db() -> AsyncSession:
    """Получение сессии"""
    async with async_session() as session:
        yield session