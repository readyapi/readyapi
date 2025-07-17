from typing import Annotated, Union

from readyapi import Cookie, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
