from typing import Annotated, Union

from readyapi import ReadyAPI, Header

app = ReadyAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
