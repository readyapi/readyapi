from readyapi import Depends, ReadyAPI
from readyapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = ReadyAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
