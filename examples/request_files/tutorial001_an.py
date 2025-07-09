from readyapi import File, ReadyAPI, UploadFile
from typing_extensions import Annotated

app = ReadyAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
