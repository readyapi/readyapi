from readyapi import ReadyAPI, Header

app = ReadyAPI()


@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
