from pydantic import BaseModel
from readyapi import ReadyAPI


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
