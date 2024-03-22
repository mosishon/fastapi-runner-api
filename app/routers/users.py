from fastapi import (APIRouter, Depends, HTTPException, Request, UploadFile,
                     status)

from app.constants import FILE_SIZE_LIMIT, RUNNER_CONTAINER_ADDRESS
from app.db.user_controller import verify_user_password
from app.dependencies import is_user_logged_in
from app.models.user import RunArguments, User
from app.utils import generate_jwt_token, http_post_request

router = APIRouter(prefix="/users", dependencies=[Depends(is_user_logged_in)])


@router.post("/login")
async def users_login(user: User, request: Request):
    vrify_result = await verify_user_password(user.username, user.password)
    if vrify_result == False:
        raise HTTPException(status_code=401, detail="Incorrect credential")
    jwt = generate_jwt_token(user.username, request.client.host)
    return {"token": jwt}


@router.post("/run-code")
async def run_code(file: UploadFile, arguments: RunArguments):
    if file.size > FILE_SIZE_LIMIT:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "File size to much.")
    else:
        resp = await http_post_request(RUNNER_CONTAINER_ADDRESS, {"file": file.file, "language": arguments.language})
        print(resp)
