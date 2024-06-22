from readyapi import ReadyAPI, Request
from readyapi.responses import HTMLResponse
from readyapi.staticfiles import StaticFiles
from readyapi.templating import Jinja2Templates

app = ReadyAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
