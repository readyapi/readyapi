from readyapi import ReadyAPI
from readyapi.middleware.gzip import GZipMiddleware

app = ReadyAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
async def main():
    return "somebigcontent"
