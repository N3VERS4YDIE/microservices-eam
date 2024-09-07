from routes.base import BaseController
from models.user import User

class UserController(BaseController):
    def __init__(self):
        super().__init__(User)
