from typing import List, Union

from readyapi import Query, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items
