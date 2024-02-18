from typing import Union

from pydantic import BaseModel, EmailStr
from readyapi import ReadyAPI

app = ReadyAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
