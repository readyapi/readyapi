import importlib

import pytest
from dirty_equals import IsDict, IsOneOf
from readyapi.testclient import TestClient

from ...utils import needs_py39, needs_py310


@pytest.fixture(
    name="client",
    params=[
        "tutorial004",
        pytest.param("tutorial004_py39", marks=needs_py39),
        pytest.param("tutorial004_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.response_model.{request.param}")

    client = TestClient(mod.app)
    return client


@pytest.mark.parametrize(
    "url,data",
    [
        ("/items/foo", {"name": "Foo", "price": 50.2}),
        (
            "/items/bar",
            {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
        ),
        (
            "/items/baz",
            {
                "name": "Baz",
                "description": None,
                "price": 50.2,
                "tax": 10.5,
                "tags": [],
            },
        ),
    ],
)
def test_get(url, data, client: TestClient):
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == data


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/items/{item_id}": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Item"}
                                }
                            },
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
                    "summary": "Read Item",
                    "operationId": "read_item_items__item_id__get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Item Id", "type": "string"},
                            "name": "item_id",
                            "in": "path",
                        }
                    ],
                }
            }
        },
        "components": {
            "schemas": {
                "Item": {
                    "title": "Item",
                    "required": IsOneOf(
                        ["name", "description", "price", "tax", "tags"],
                        # TODO: remove when deprecating Pydantic v1
                        ["name", "price"],
                    ),
                    "type": "object",
                    "properties": {
                        "name": {"title": "Name", "type": "string"},
                        "price": {"title": "Price", "type": "number"},
                        "description": IsDict(
                            {
                                "title": "Description",
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {"title": "Description", "type": "string"}
                        ),
                        "tax": {"title": "Tax", "type": "number", "default": 10.5},
                        "tags": {
                            "title": "Tags",
                            "type": "array",
                            "items": {"type": "string"},
                            "default": [],
                        },
                    },
                },
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
