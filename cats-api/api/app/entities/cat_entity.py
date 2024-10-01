from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField

from app.entities.base_entity import BaseEntity
from app.entities.owner_entity import OwnerEntity


class CatEntity(BaseEntity):
    id = IntegerField(primary_key=True)
    name = CharField()
    birthdate = DateTimeField(default=datetime.now)
    description = CharField(max_length=500)
    owner = ForeignKeyField(OwnerEntity, backref="cats")
