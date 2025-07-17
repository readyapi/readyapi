from readyapi import ReadyAPI

my_awesome_api = ReadyAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
