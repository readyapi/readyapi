from readyapi import ReadyAPI
from readyapi.responses import PlainTextResponse

app = ReadyAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"
