from typing import Annotated, List, Union

from readyapi import ReadyAPI, Header

app = ReadyAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}
