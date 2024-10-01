from fastapi import APIRouter

from app.controllers.cat_controller import CatController

cat_controller = CatController()

cat_router = APIRouter()
cat_router.include_router(cat_controller.get_router(), prefix="/cats", tags=["cats"])
