from app.controllers.base_controller import BaseController
from app.entities.cat_entity import CatEntity
from app.models.cat_model import CatModel
from app.services.cat_service import CatService


class CatController(BaseController):
    def __init__(self):
        super().__init__(CatModel, CatEntity, CatService)
