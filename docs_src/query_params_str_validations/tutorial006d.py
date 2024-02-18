from pydantic import Required
from readyapi import Query, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
