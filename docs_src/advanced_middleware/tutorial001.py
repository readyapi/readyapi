from readyapi import ReadyAPI
from readyapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = ReadyAPI()

app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def main():
    return {"message": "Hello World"}
