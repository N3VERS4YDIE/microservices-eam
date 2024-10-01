import os
from dotenv import load_dotenv
from peewee import MySQLDatabase

from app.entities.cat_entity import CatEntity
from app.entities.owner_entity import OwnerEntity

load_dotenv()

db = MySQLDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
)

db.connect()
db.create_tables([OwnerEntity, CatEntity])
