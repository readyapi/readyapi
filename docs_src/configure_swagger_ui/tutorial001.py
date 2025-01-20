from readyapi import ReadyAPI

app = ReadyAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
