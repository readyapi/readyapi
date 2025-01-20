from readyapi import ReadyAPI

from . import a, b

app = ReadyAPI()

app.include_router(a.router, prefix="/a")
app.include_router(b.router, prefix="/b")
