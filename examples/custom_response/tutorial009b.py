from readyapi import ReadyAPI
from readyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = ReadyAPI()


@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path
