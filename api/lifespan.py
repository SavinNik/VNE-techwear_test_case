from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.async_session import init_db, async_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await async_engine.dispose()