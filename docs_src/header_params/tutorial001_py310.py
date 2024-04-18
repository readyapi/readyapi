from readyapi import ReadyAPI, Header

app = ReadyAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
