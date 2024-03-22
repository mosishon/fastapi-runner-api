from pydantic import BaseModel


class AdminLogin(BaseModel):
    username: str
    password: str


class Admin(BaseModel):
    username: str
    password: str
    # MAYBE MORE
