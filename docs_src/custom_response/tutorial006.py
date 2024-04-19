from readyapi import ReadyAPI
from readyapi.responses import RedirectResponse

app = ReadyAPI()


@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")
