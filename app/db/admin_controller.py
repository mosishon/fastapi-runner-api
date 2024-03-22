from app.db.redis_client import redis_client
from app.utils import get_password_hash, verify_password


async def create_super_user(username: str, password: str):
    super_user = await redis_client.get("superuser")
    if super_user is not None:
        return False
    await redis_client.set("superuser", f"{username}:{get_password_hash(password)}")
    return True


async def get_admin(username: str, password: str):
    super_user = await redis_client.get("superuser")
    if super_user is None:
        return False

    user, passw = super_user.split(":")
    if username == user and verify_password(password, passw):
        return True
