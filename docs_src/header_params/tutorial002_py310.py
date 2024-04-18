from readyapi import ReadyAPI, Header

app = ReadyAPI()


@app.get("/items/")
async def read_items(
    strange_header: str | None = Header(default=None, convert_underscores=False),
):
    return {"strange_header": strange_header}
