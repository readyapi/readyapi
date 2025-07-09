from readyapi import ReadyAPI
from readyapi.middleware.trustedhost import TrustedHostMiddleware

app = ReadyAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
