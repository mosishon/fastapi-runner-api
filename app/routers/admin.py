from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.db.admin_controller import create_super_user, get_admin
from app.db.user_controller import create_user
from app.dependencies import is_admin
from app.exceptions.user import UserAlreadyExists
from app.models.admin import AdminLogin
from app.models.token import Token
from app.models.user import User
from app.utils import generate_jwt_token, get_ip

router = APIRouter(prefix="/admin", dependencies=[Depends(is_admin)])


@router.post("/login")
async def admin_login(user: AdminLogin, request: Request):
    admin = await get_admin(user.username, user.password)

    if not admin:
        raise HTTPException(status_code=401, detail="Incorrect credential")
    jwt = generate_jwt_token(user.username, await get_ip(request))
    return {"token": jwt}


@router.post("/new-user")
async def new_user(user: User, token: Token = Depends(is_admin)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    print(token)
    try:
        user_dict = await create_user(user)
    except UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User Exists")

    return {"message": "User created", "user": user_dict}
