from typing import Annotated

from readyapi import Cookie, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
