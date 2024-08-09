from readyapi import ReadyAPI, Query
from typing_extensions import Annotated

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items
