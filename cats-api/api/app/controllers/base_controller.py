from typing import Dict, Generic, List, Type, TypeVar

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.db.db import get_db
from app.services.base_service import BaseService

TModel = TypeVar("TModel")
TEntity = TypeVar("TEntity", bound=BaseModel)


class BaseController:

    def __init__(
        self, model: Type[TModel], entity: Type[TEntity], service: BaseService
    ):
        self.model = model
        self.entity = entity
        self.router = APIRouter()
        self.service = service

        self.router.add_api_route("/", self.create, methods=["POST"])
        self.router.add_api_route("/", self.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_by_id, methods=["GET"])
        self.router.add_api_route("/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete, methods=["DELETE"])

    def get_router(self):
        return self.router

    def get_all(self) -> List[TModel]:
        return self.service.get_all()

    def get_by_id(self, id: int) -> TModel:
        model = self.service.get_by_id(id)
        if model is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return model

    def create(self, model: TModel) -> TModel:
        return self.service.create(model)

    def update(self, id: int, model_data: TModel) -> TModel:
        model = self.service.update(model_data)

        if model is None:
            raise HTTPException(status_code=404, detail="Not found")

        return model

    def delete(self, id: int):
        is_deleted = self.service.delete(id)

        if not is_deleted:
            raise HTTPException(status_code=404, detail="Not found")

        return {"msg": "Item deleted successfully"}
