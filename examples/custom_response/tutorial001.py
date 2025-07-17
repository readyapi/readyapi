from readyapi import ReadyAPI
from readyapi.responses import UJSONResponse

app = ReadyAPI()


@app.get("/items/", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]
