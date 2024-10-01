from fastapi import APIRouter

from app.controllers.owner_controller import OwnerController

owner_controller = OwnerController()

owner_router = APIRouter()
owner_router.include_router(
    owner_controller.get_router(), prefix="/owners", tags=["owners"]
)
