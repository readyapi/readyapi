from typing import Union

from readyapi import Query, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
