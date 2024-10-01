from app.entities.owner_entity import OwnerEntity
from app.repositories.base_repository import BaseRepository


class OwnerService(BaseRepository):
    def __init__(self):
        super().__init__(OwnerEntity)
