from readyapi.testclient import TestClient

from examples.handling_errors.tutorial003 import app

client = TestClient(app)


def test_get():
    response = client.get("/unicorns/shinny")
    assert response.status_code == 200, response.text
    assert response.json() == {"unicorn_name": "shinny"}


def test_get_exception():
    response = client.get("/unicorns/yolo")
    assert response.status_code == 418, response.text
    assert response.json() == {
        "message": "Oops! yolo did something. There goes a rainbow..."
    }


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/unicorns/{name}": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                    "summary": "Read Unicorn",
                    "operationId": "read_unicorn_unicorns__name__get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Name", "type": "string"},
                            "name": "name",
                            "in": "path",
                        }
                    ],
                }
            }
        },
        "components": {
            "schemas": {
                "ValidationError": {
                    "title": "ValidationError",
                    "required": ["loc", "msg", "type"],
                    "type": "object",
                    "properties": {
                        "loc": {
                            "title": "Location",
                            "type": "array",
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                        },
                        "msg": {"title": "Message", "type": "string"},
                        "type": {"title": "Error Type", "type": "string"},
                    },
                },
                "HTTPValidationError": {
                    "title": "HTTPValidationError",
                    "type": "object",
                    "properties": {
                        "detail": {
                            "title": "Detail",
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                        }
                    },
                },
            }
        },
    }
