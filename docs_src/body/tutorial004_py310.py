from pydantic import BaseModel
from readyapi import ReadyAPI


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = ReadyAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
