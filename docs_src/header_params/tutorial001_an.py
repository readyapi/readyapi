from typing import Union

from readyapi import Header, ReadyAPI
from typing_extensions import Annotated

app = ReadyAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
