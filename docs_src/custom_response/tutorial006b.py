from readyapi import ReadyAPI
from readyapi.responses import RedirectResponse

app = ReadyAPI()


@app.get("/readyapi", response_class=RedirectResponse)
async def redirect_readyapi():
    return "https://readyapi.khulnasoft.com"
