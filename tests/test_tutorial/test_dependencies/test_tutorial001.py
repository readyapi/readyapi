import importlib

import pytest
from dirty_equals import IsDict
from readyapi.testclient import TestClient

from ...utils import needs_py39, needs_py310


@pytest.fixture(
    name="client",
    params=[
        "tutorial001",
        pytest.param("tutorial001_py310", marks=needs_py310),
        "tutorial001_an",
        pytest.param("tutorial001_an_py39", marks=needs_py39),
        pytest.param("tutorial001_an_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.dependencies.{request.param}")

    client = TestClient(mod.app)
    return client


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/items", 200, {"q": None, "skip": 0, "limit": 100}),
        ("/items?q=foo", 200, {"q": "foo", "skip": 0, "limit": 100}),
        ("/items?q=foo&skip=5", 200, {"q": "foo", "skip": 5, "limit": 100}),
        ("/items?q=foo&skip=5&limit=30", 200, {"q": "foo", "skip": 5, "limit": 30}),
        ("/users", 200, {"q": None, "skip": 0, "limit": 100}),
    ],
)
def test_get(path, expected_status, expected_response, client: TestClient):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response


def test_openapi_schema(client: TestClient):
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
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "parameters": [
                        {
                            "required": False,
                            "schema": IsDict(
                                {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "title": "Q",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {"title": "Q", "type": "string"}
                            ),
                            "name": "q",
                            "in": "query",
                        },
                        {
                            "required": False,
                            "schema": {
                                "title": "Skip",
                                "type": "integer",
                                "default": 0,
                            },
                            "name": "skip",
                            "in": "query",
                        },
                        {
                            "required": False,
                            "schema": {
                                "title": "Limit",
                                "type": "integer",
                                "default": 100,
                            },
                            "name": "limit",
                            "in": "query",
                        },
                    ],
                }
            },
            "/users/": {
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
                    "summary": "Read Users",
                    "operationId": "read_users_users__get",
                    "parameters": [
                        {
                            "required": False,
                            "schema": IsDict(
                                {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "title": "Q",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {"title": "Q", "type": "string"}
                            ),
                            "name": "q",
                            "in": "query",
                        },
                        {
                            "required": False,
                            "schema": {
                                "title": "Skip",
                                "type": "integer",
                                "default": 0,
                            },
                            "name": "skip",
                            "in": "query",
                        },
                        {
                            "required": False,
                            "schema": {
                                "title": "Limit",
                                "type": "integer",
                                "default": 100,
                            },
                            "name": "limit",
                            "in": "query",
                        },
                    ],
                }
            },
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
