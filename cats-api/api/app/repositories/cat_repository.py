from app.entities.cat_entity import CatEntity
from app.repositories.base_repository import BaseRepository


class CatRepository(BaseRepository):
    def __init__(self):
        super().__init__(CatEntity)
