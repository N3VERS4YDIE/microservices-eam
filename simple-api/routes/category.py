from routes.base import BaseController
from models.category import Category

class CategoryController(BaseController):
    def __init__(self):
        super().__init__(Category)