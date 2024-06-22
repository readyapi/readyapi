from readyapi import ReadyAPI
from readyapi.responses import RedirectResponse

app = ReadyAPI()


@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"
