from fastapi import APIRouter, Depends, HTTPException, Request

from app.db.user_controller import verify_user_password
from app.dependencies import is_user_logged_in
from app.models.user import User
from app.utils import generate_jwt_token

router = APIRouter(prefix="/users", dependencies=[Depends(is_user_logged_in)])


@router.post("/login")
async def users_login(user: User, request: Request):
    vrify_result = await verify_user_password(user.username, user.password)
    if vrify_result == False:
        raise HTTPException(status_code=401, detail="Incorrect credential")
    jwt = generate_jwt_token(user.username, request.client.host)
    return {"token": jwt}
