import importlib

import pytest
from dirty_equals import IsDict
from readyapi.testclient import TestClient

from ...utils import needs_py39, needs_py310


@pytest.fixture(
    name="client",
    params=[
        "tutorial002",
        pytest.param("tutorial002_py310", marks=needs_py310),
        "tutorial002_an",
        pytest.param("tutorial002_an_py39", marks=needs_py39),
        pytest.param("tutorial002_an_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.header_params.{request.param}")

    client = TestClient(mod.app)
    return client


@pytest.mark.parametrize(
    "path,headers,expected_status,expected_response",
    [
        ("/items", None, 200, {"strange_header": None}),
        ("/items", {"X-Header": "notvalid"}, 200, {"strange_header": None}),
        (
            "/items",
            {"strange_header": "ReadyAPI test"},
            200,
            {"strange_header": "ReadyAPI test"},
        ),
        (
            "/items",
            {"strange-header": "Not really underscore"},
            200,
            {"strange_header": None},
        ),
    ],
)
def test(path, headers, expected_status, expected_response, client: TestClient):
    response = client.get(path, headers=headers)
    assert response.status_code == expected_status
    assert response.json() == expected_response


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200
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
                                    "title": "Strange Header",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {"title": "Strange Header", "type": "string"}
                            ),
                            "name": "strange_header",
                            "in": "header",
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
