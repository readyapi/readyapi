import pytest
from readyapi import ReadyAPI, Request
from readyapi.testclient import TestClient

app = ReadyAPI()

@app.get("/items/")
async def read_items(request: Request):
    return {"method": request.method, "url": str(request.url)}

@app.post("/items/")
async def create_item(request: Request):
    return {"method": request.method, "url": str(request.url)}

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"method": "GET", "url": "http://testserver/items/"}

def test_create_item():
    response = client.post("/items/")
    assert response.status_code == 200
    assert response.json() == {"method": "POST", "url": "http://testserver/items/"}

def test_invalid_method():
    response = client.delete("/items/")
    assert response.status_code == 405
