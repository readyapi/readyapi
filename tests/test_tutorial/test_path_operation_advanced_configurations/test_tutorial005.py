from readyapi.testclient import TestClient

from examples.path_operation_advanced_configuration.tutorial005 import app

client = TestClient(app)


def test_get():
    response = client.get("/items/")
    assert response.status_code == 200, response.text


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "x-aperture-labs-portal": "blue",
                }
            }
        },
    }
