from readyapi import ReadyAPI
from readyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = ReadyAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)
