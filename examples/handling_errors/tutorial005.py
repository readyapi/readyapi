from pydantic import BaseModel
from readyapi import ReadyAPI, Request, status
from readyapi.encoders import jsonable_encoder
from readyapi.exceptions import RequestValidationError
from readyapi.responses import JSONResponse

app = ReadyAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item
