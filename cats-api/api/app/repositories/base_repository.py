from typing import Generic, List, Optional, Type, TypeVar

from peewee import Model

T = TypeVar("T", bound=Model)


class BaseRepository:
    def __init__(self, entity: Type[T]):
        self.model = entity

    def get_all(self) -> List[T]:
        return list(self.model.select())

    def get_by_id(self, entity_id: int) -> Optional[T]:
        try:
            return self.model.get(self.model.id == entity_id)
        except self.model.DoesNotExist:
            return None

    def create(self, entity_data: dict) -> T:
        return self.model.create(**entity_data)

    def delete(self, entity_id: int) -> bool:
        query = self.model.delete().where(self.model.id == entity_id)
        return query.execute() > 0
