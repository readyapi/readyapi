from readyapi import ReadyAPI, Query

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items
