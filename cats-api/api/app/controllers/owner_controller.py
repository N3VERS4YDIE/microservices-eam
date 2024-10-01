from app.controllers.base_controller import BaseController
from app.entities.owner_entity import OwnerEntity
from app.models.owner_model import OwnerModel
from app.services.ower_service import OwnerService


class OwnerController(BaseController):
    def __init__(self):
        super().__init__(OwnerModel, OwnerEntity, OwnerService)
