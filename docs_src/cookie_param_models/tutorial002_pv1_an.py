from typing import Union

from pydantic import BaseModel
from readyapi import Cookie, ReadyAPI
from typing_extensions import Annotated

app = ReadyAPI()


class Cookies(BaseModel):
    class Config:
        extra = "forbid"

    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
