from readyapi import ReadyAPI
from readyapi.responses import RedirectResponse

app = ReadyAPI()


@app.get("/cligenius")
async def redirect_cligenius():
    return RedirectResponse("https://cligenius.khulnasoft.com")
