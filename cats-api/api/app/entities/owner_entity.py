from peewee import CharField, IntegerField

from app.entities.base_entity import BaseEntity


class OwnerEntity(BaseEntity):
    id = IntegerField(primary_key=True)
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
