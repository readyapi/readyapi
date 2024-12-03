import pytest
from readyapi import ReadyAPI, Response, JSONResponse, XMLResponse, UJSONResponse, ORJSONResponse, CustomResponse
from readyapi.testclient import TestClient

app = ReadyAPI()

@app.get("/json")
async def get_json():
    return JSONResponse({"message": "Hello, World!"})

@app.get("/xml")
async def get_xml():
    return XMLResponse({"message": "Hello, World!"})

@app.get("/ujson")
async def get_ujson():
    return UJSONResponse({"message": "Hello, World!"})

@app.get("/orjson")
async def get_orjson():
    return ORJSONResponse({"message": "Hello, World!"})

@app.get("/custom")
async def get_custom():
    return CustomResponse({"message": "Hello, World!"})

client = TestClient(app)

def test_get_json():
    response = client.get("/json")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_xml():
    response = client.get("/xml")
    assert response.status_code == 200
    assert response.text == '<root><message>Hello, World!</message></root>'

def test_get_ujson():
    response = client.get("/ujson")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_orjson():
    response = client.get("/orjson")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_custom():
    response = client.get("/custom")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_invalid_custom_response():
    with pytest.raises(TypeError):
        CustomResponse(12345)
