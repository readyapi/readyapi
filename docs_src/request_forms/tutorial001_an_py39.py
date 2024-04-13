from typing import Annotated

from readyapi import ReadyAPI, Form

app = ReadyAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
