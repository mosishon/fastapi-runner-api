from datetime import datetime, timedelta

try:
    from datetime import UTC
except ImportError:
    from datetime import timezone
    UTC = timezone.utc
import httpx
import jwt
from fastapi import Request
from passlib.context import CryptContext

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def generate_jwt_token(user_name: str, ip: str = "") -> str:
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"uid": str(user_name), "exp": expire, "ip": ip}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_uid_from_token(token: str) -> str:
    try:
        dec = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return dec.get("uid")
    except:
        return ""


def get_ip_from_token(token: str) -> str:
    try:
        dec = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return dec.get("ip")
    except:
        return ""


async def http_get_request(url: str, params: dict | None = None, headers: dict | None = None):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, headers=headers)
            # response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except httpx.HTTPError as exc:
            # Handle HTTP errors here
            raise exc


async def http_post_request(url: str, data: dict, files: dict | None = None, headers: dict | None = None):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, data=data, files=files, headers=headers)
            # response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except httpx.HTTPError as exc:
            # Handle HTTP errors here
            raise exc


async def get_ip(request: Request) -> str:
    return request.headers.get("x-forwarded-for", request.client.host)
