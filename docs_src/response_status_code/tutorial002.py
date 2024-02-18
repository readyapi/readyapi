from readyapi import ReadyAPI, status

app = ReadyAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
