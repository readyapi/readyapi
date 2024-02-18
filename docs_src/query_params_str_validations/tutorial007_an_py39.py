from typing import Annotated, Union

from readyapi import Query, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[Union[str, None], Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
