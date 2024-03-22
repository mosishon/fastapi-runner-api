from typing import Annotated

from fastapi import (APIRouter, Depends, Form, HTTPException, Request,
                     UploadFile, status)

from app.constants import FILE_SIZE_LIMIT, RUNNER_ADDRESS
from app.db.user_controller import verify_user_password
from app.dependencies import is_user_logged_in
from app.models.user import UserLogin
from app.utils import generate_jwt_token, get_ip, http_post_request

router = APIRouter(prefix="/users", dependencies=[Depends(is_user_logged_in)])


@router.post("/login")
async def users_login(user: UserLogin, request: Request):
    vrify_result = await verify_user_password(user.username, user.password)
    if vrify_result == False:
        raise HTTPException(status_code=401, detail="Incorrect credential")
    jwt = generate_jwt_token(user.username, await get_ip(request))
    return {"token": jwt}


@router.post("/run-code")
async def run_code(request: Request, file: UploadFile, language: Annotated[str, Form()], args: Annotated[str, Form()]):
    if file.size > FILE_SIZE_LIMIT:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "File size to much.")
    else:
        print(request.headers)
        try:
            resp = await http_post_request(f"{RUNNER_ADDRESS}/run", {"language": language, "args": args}, files={"file": file.file})
            resp['ip'] = await get_ip(request)
            return resp
        except:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, "Unknown error")
