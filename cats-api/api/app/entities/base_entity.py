from peewee import (
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
)

from app.db import db
from app.entities.cat_entity import CatEntity
from app.entities.owner_entity import OwnerEntity


class BaseEntity(Model):
    class Meta:
        database = db
