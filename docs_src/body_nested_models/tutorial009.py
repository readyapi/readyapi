from typing import Dict

from readyapi import ReadyAPI

app = ReadyAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
