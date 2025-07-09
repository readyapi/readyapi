from datetime import datetime
from typing import Union

from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.encoders import jsonable_encoder
from readyapi.responses import JSONResponse


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = ReadyAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)
