from typing import List, Union

from readyapi import Header, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}
