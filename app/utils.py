from datetime import UTC, datetime, timedelta

import jwt
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
