from readyapi import ReadyAPI, Form
from typing_extensions import Annotated

app = ReadyAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
