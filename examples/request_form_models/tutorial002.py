from pydantic import BaseModel
from readyapi import Form, ReadyAPI

app = ReadyAPI()


class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/login/")
async def login(data: FormData = Form()):
    return data
