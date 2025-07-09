from typing import List

from pydantic import BaseModel, HttpUrl
from readyapi import ReadyAPI

app = ReadyAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
