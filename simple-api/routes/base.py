from fastapi import APIRouter, Body
from pydantic import BaseModel
from models.user import User
import json
from uuid import uuid4
from datetime import datetime

def get_id():
    return uuid4().int

def get_time():
    return datetime.now().isoformat()

class BaseController:

    def __init__(self, model: BaseModel):
        self.model = model
        self.route = APIRouter()

        model_schema = self.model.model_json_schema()

        default_values = {
            "string": "string",
            "integer": 0,
            "number": 0.0,
            "boolean": False,
            "array": [],
            "object": {}
        }

        special_values = {
            "id": get_id,
            "at": get_time
        }

        model_example = {
            prop: default_values.get(details["type"], f"<{prop}>")
            for prop, details in model_schema.get('properties', {}).items()
        }

        model_example = json.dumps(json.loads(
            str(model_example).replace("'", '"')), indent=4).replace("\n", "<br>").replace(" ", "&nbsp;")

        self.route.add_api_route("/", self.get_all, methods=["GET"])
        self.route.add_api_route("/{id}", self.get_by_id, methods=["GET"])
        self.route.add_api_route("/", self.save, methods=["POST"],
                                 response_model=self.model,  description=model_example)
        self.route.add_api_route("/{id}", self.update_by_id,
                                 methods=["PUT"], response_model=self.model,  description=model_example)
        self.route.add_api_route("/{id}", self.delete_by_id, methods=["DELETE"], response_model=self.model)

        self.db = {}

    def get_all(self):
        return self.db

    def get_by_id(self, id: int):
        return self.db[id]

    def save(self, entity: BaseModel = Body()):
        key = len(self.db) + 1
        self.db[key] = entity.dict()
        return {"message": "Saved", "entity": entity}

    def update_by_id(self, id: int, entity: BaseModel = Body()):
        if id in self.db:
            self.db[id] = entity.dict()
            return {"message": "Updated", "id": id, "entity": entity}
        else:
            return {"message": "User not found", "id": id}

    def delete_by_id(self, id: int):
        if id in self.db:
            del self.db[id]
            return {"message": "Deleted", "id": id}
        else:
            return {"message": "User not found", "id": id}
