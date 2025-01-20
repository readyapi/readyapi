from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
