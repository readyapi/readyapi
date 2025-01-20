from readyapi import ReadyAPI
from readyapi.staticfiles import StaticFiles

app = ReadyAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
