class BaseEx(Exception):
    code: int
    message: str


class UserAlreadyExists(BaseEx):
    code = -1

    def __init__(self, username: str):
        self.message = F"User `{username}` alredy exists. "


class UserNotExists(BaseEx):
    code = -1

    def __init__(self, username: str):
        self.message = F"User `{username}` not exists. "
