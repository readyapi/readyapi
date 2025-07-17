from readyapi import ReadyAPI
from readyapi.responses import ORJSONResponse

app = ReadyAPI(default_response_class=ORJSONResponse)


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]
