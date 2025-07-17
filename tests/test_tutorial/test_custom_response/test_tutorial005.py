from readyapi.testclient import TestClient

from examples.custom_response.tutorial005 import app

client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.text == "Hello World"


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/": {
                "get": {
                    "summary": "Main",
                    "operationId": "main__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"text/plain": {"schema": {"type": "string"}}},
                        }
                    },
                }
            }
        },
    }
