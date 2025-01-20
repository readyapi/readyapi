from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
