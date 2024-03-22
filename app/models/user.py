from typing import Annotated

from fastapi import Form
from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    password: str
    # MAYBE MORE

    def to_dict(self):
        return {"name": self.name, "username": self.username, "password": self.password}


class UserLogin(BaseModel):
    username: str
    password: str
