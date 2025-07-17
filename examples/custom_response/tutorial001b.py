from readyapi import ReadyAPI
from readyapi.responses import ORJSONResponse

app = ReadyAPI()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
