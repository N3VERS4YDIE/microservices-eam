from app.repositories.base_repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id: int) -> dict:
        return self.repository.get_by_id(entity_id)

    def create(self, entity_data: dict) -> dict:
        return self.repository.create(entity_data)

    def update(self, entity_data: dict) -> dict:
        existing_entity = self.get_by_id(entity_data.get("id"))
        if existing_entity is None:
            return None

        for key, value in entity_data.items():
            setattr(existing_entity, key, value)

        return existing_entity

    def delete(self, entity_id: int):
        return self.repository.delete(entity_id)
