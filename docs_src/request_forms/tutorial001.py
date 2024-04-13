from readyapi import ReadyAPI, Form

app = ReadyAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
