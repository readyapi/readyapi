from readyapi import ReadyAPI
from readyapi.responses import StreamingResponse

app = ReadyAPI()


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())
