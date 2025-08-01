import importlib

import pytest
from readyapi.testclient import TestClient

from ...utils import needs_py39, needs_py310, needs_pydanticv2


@pytest.fixture(
    name="client",
    params=[
        "tutorial002",
        pytest.param("tutorial002_py310", marks=needs_py310),
        pytest.param("tutorial002_py39", marks=needs_py39),
    ],
)
def get_client(request: pytest.FixtureRequest) -> TestClient:
    mod = importlib.import_module(f"examples.separate_openapi_schemas.{request.param}")

    client = TestClient(mod.app)
    return client


def test_create_item(client: TestClient) -> None:
    response = client.post("/items/", json={"name": "Foo"})
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo", "description": None}


def test_read_items(client: TestClient) -> None:
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {
            "name": "Portal Gun",
            "description": "Device to travel through the multi-rick-verse",
        },
        {"name": "Plumbus", "description": None},
    ]


@needs_pydanticv2
def test_openapi_schema(client: TestClient) -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "items": {"$ref": "#/components/schemas/Item"},
                                        "type": "array",
                                        "title": "Response Read Items Items  Get",
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create Item",
                    "operationId": "create_item_items__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Item"}
                            }
                        },
                        "required": True,
                    },
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
                },
            }
        },
        "components": {
            "schemas": {
                "HTTPValidationError": {
                    "properties": {
                        "detail": {
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                            "type": "array",
                            "title": "Detail",
                        }
                    },
                    "type": "object",
                    "title": "HTTPValidationError",
                },
                "Item": {
                    "properties": {
                        "name": {"type": "string", "title": "Name"},
                        "description": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "title": "Description",
                        },
                    },
                    "type": "object",
                    "required": ["name"],
                    "title": "Item",
                },
                "ValidationError": {
                    "properties": {
                        "loc": {
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                            "type": "array",
                            "title": "Location",
                        },
                        "msg": {"type": "string", "title": "Message"},
                        "type": {"type": "string", "title": "Error Type"},
                    },
                    "type": "object",
                    "required": ["loc", "msg", "type"],
                    "title": "ValidationError",
                },
            }
        },
    }
