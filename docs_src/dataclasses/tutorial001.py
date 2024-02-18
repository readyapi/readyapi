from dataclasses import dataclass
from typing import Union

from readyapi import ReadyAPI


@dataclass
class Item:
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
