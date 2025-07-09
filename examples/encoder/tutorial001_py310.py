from datetime import datetime

from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.encoders import jsonable_encoder

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = ReadyAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
