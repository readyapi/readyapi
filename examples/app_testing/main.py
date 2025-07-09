from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
