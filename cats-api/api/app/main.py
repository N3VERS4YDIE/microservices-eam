from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database import Settings
from app.routes.cat_route import cat_router
from app.routes.owner_route import owner_router

app = FastAPI()
settings = Settings()

app.include_router(owner_router)
app.include_router(cat_router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
