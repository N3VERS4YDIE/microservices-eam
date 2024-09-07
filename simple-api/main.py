from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.user import UserController
from routes.category import CategoryController


app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

app.include_router(UserController().route, prefix="/user", tags=["User"])
app.include_router(CategoryController().route, prefix="/categories", tags=["Categories"])
