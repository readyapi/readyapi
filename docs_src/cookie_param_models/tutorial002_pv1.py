from typing import Union

from pydantic import BaseModel
from readyapi import Cookie, ReadyAPI

app = ReadyAPI()


class Cookies(BaseModel):
    class Config:
        extra = "forbid"

    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None


@app.get("/items/")
async def read_items(cookies: Cookies = Cookie()):
    return cookies
