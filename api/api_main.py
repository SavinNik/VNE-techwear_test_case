from fastapi import FastAPI
from api.lifespan import lifespan
from api.endpoints import routers as catalog

app = FastAPI(
    title="API VNE_techwear",
    lifespan=lifespan
)

app.include_router(catalog.router)

@app.get("/")
async def root():
    return {"message": "VNE_techwear", "docs": "/docs"}