import importlib

import pytest
from dirty_equals import IsDict
from inline_snapshot import snapshot
from readyapi.testclient import TestClient

from tests.utils import needs_py39, needs_py310


@pytest.fixture(
    name="client",
    params=[
        "tutorial003",
        pytest.param("tutorial003_py39", marks=needs_py39),
        pytest.param("tutorial003_py310", marks=needs_py310),
        "tutorial003_an",
        pytest.param("tutorial003_an_py39", marks=needs_py39),
        pytest.param("tutorial003_an_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.header_param_models.{request.param}")

    client = TestClient(mod.app)
    return client


def test_header_param_model(client: TestClient):
    response = client.get(
        "/items/",
        headers=[
            ("save_data", "true"),
            ("if_modified_since", "yesterday"),
            ("traceparent", "123"),
            ("x_tag", "one"),
            ("x_tag", "two"),
        ],
    )
    assert response.status_code == 200
    assert response.json() == {
        "host": "testserver",
        "save_data": True,
        "if_modified_since": "yesterday",
        "traceparent": "123",
        "x_tag": ["one", "two"],
    }


def test_header_param_model_no_underscore(client: TestClient):
    response = client.get(
        "/items/",
        headers=[
            ("save-data", "true"),
            ("if-modified-since", "yesterday"),
            ("traceparent", "123"),
            ("x-tag", "one"),
            ("x-tag", "two"),
        ],
    )
    assert response.status_code == 422
    assert response.json() == snapshot(
        {
            "detail": [
                IsDict(
                    {
                        "type": "missing",
                        "loc": ["header", "save_data"],
                        "msg": "Field required",
                        "input": {
                            "host": "testserver",
                            "traceparent": "123",
                            "x_tag": [],
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate",
                            "connection": "keep-alive",
                            "user-agent": "testclient",
                            "save-data": "true",
                            "if-modified-since": "yesterday",
                            "x-tag": "two",
                        },
                    }
                )
                | IsDict(
                    # TODO: remove when deprecating Pydantic v1
                    {
                        "type": "value_error.missing",
                        "loc": ["header", "save_data"],
                        "msg": "field required",
                    }
                )
            ]
        }
    )


def test_header_param_model_defaults(client: TestClient):
    response = client.get("/items/", headers=[("save_data", "true")])
    assert response.status_code == 200
    assert response.json() == {
        "host": "testserver",
        "save_data": True,
        "if_modified_since": None,
        "traceparent": None,
        "x_tag": [],
    }


def test_header_param_model_invalid(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 422
    assert response.json() == snapshot(
        {
            "detail": [
                IsDict(
                    {
                        "type": "missing",
                        "loc": ["header", "save_data"],
                        "msg": "Field required",
                        "input": {
                            "x_tag": [],
                            "host": "testserver",
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate",
                            "connection": "keep-alive",
                            "user-agent": "testclient",
                        },
                    }
                )
                | IsDict(
                    # TODO: remove when deprecating Pydantic v1
                    {
                        "type": "value_error.missing",
                        "loc": ["header", "save_data"],
                        "msg": "field required",
                    }
                )
            ]
        }
    )


def test_header_param_model_extra(client: TestClient):
    response = client.get(
        "/items/", headers=[("save_data", "true"), ("tool", "plumbus")]
    )
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "host": "testserver",
            "save_data": True,
            "if_modified_since": None,
            "traceparent": None,
            "x_tag": [],
        }
    )


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "ReadyAPI", "version": "0.1.0"},
            "paths": {
                "/items/": {
                    "get": {
                        "summary": "Read Items",
                        "operationId": "read_items_items__get",
                        "parameters": [
                            {
                                "name": "host",
                                "in": "header",
                                "required": True,
                                "schema": {"type": "string", "title": "Host"},
                            },
                            {
                                "name": "save_data",
                                "in": "header",
                                "required": True,
                                "schema": {"type": "boolean", "title": "Save Data"},
                            },
                            {
                                "name": "if_modified_since",
                                "in": "header",
                                "required": False,
                                "schema": IsDict(
                                    {
                                        "anyOf": [{"type": "string"}, {"type": "null"}],
                                        "title": "If Modified Since",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "type": "string",
                                        "title": "If Modified Since",
                                    }
                                ),
                            },
                            {
                                "name": "traceparent",
                                "in": "header",
                                "required": False,
                                "schema": IsDict(
                                    {
                                        "anyOf": [{"type": "string"}, {"type": "null"}],
                                        "title": "Traceparent",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "type": "string",
                                        "title": "Traceparent",
                                    }
                                ),
                            },
                            {
                                "name": "x_tag",
                                "in": "header",
                                "required": False,
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "default": [],
                                    "title": "X Tag",
                                },
                            },
                        ],
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
                    }
                }
            },
            "components": {
                "schemas": {
                    "HTTPValidationError": {
                        "properties": {
                            "detail": {
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                                "type": "array",
                                "title": "Detail",
                            }
                        },
                        "type": "object",
                        "title": "HTTPValidationError",
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
    )
