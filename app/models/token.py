from pydantic import BaseModel


class Token(BaseModel):
    uid: str
    ip: str
