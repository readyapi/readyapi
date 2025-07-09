from readyapi import ReadyAPI

app = ReadyAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
