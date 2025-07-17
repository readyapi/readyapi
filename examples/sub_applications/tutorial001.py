from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = ReadyAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
