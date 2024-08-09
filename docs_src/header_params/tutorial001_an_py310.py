from typing import Annotated

from readyapi import Header, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
