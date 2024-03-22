from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

from app.models.token import Token
from app.utils import get_ip_from_token, get_uid_from_token

oauth_admin = OAuth2PasswordBearer("/admin/login")
oauthـuser = OAuth2PasswordBearer("/users/login")


async def is_admin(request: Request) -> Token | None:
    if request.url_for("admin_login") != request.url:

        token = await oauth_admin(request)
        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credential.")
        admin = get_uid_from_token(token)
        ip = get_ip_from_token(token)
        print(f"Token ip:{ip} - request ip:{request.client.host}")
        if ip != request.client.host:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Ip Changed login again")

        token = Token(uid=admin, ip=ip)
        return token
    return None


async def is_user_logged_in(request: Request):
    if request.url_for("users_login") != request.url:
        token = await oauthـuser(request)
        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credential.")
        user = get_uid_from_token(token)
        ip = get_ip_from_token(token)
        print(f"Token ip:{ip} - request ip:{request.client.host}")
        if ip != request.client.host:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Ip Changed login again")

        token = Token(uid=user, ip=ip)
        return token
