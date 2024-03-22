import ast
import typing

from app.db.redis_client import redis_client
from app.exceptions.user import UserAlreadyExists, UserNotExists
from app.models.user import User
from app.utils import get_password_hash, verify_password


async def create_user(user: User) -> dict:
    user_ins = await redis_client.get(f"user.{user.username}")
    if user_ins is not None:
        raise UserAlreadyExists(user.username)

    user_dict = user.to_dict()
    user_dict.update({"password": get_password_hash(user_dict['password'])})
    await redis_client.set(f"user.{user.username}", str(user_dict))
    return user_dict


async def get_user(username: str) -> dict:
    user = await redis_client.get(f"user.{username}")
    if user is None:
        raise UserNotExists(username)
    return typing.cast(dict, ast.literal_eval(user))


async def verify_user_password(username: str, password: str) -> bool:
    user = await redis_client.get(f"user.{username}")
    if user is None:
        raise UserNotExists(username)
    else:
        user_dict: dict = typing.cast(dict, ast.literal_eval(user))
        return verify_password(password, user_dict.get('password'))
