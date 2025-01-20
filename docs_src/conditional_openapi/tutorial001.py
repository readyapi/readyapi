from pydantic_settings import BaseSettings
from readyapi import ReadyAPI


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()

app = ReadyAPI(openapi_url=settings.openapi_url)


@app.get("/")
def root():
    return {"message": "Hello World"}
