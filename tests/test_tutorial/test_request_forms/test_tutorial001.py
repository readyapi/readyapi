import importlib

import pytest
from dirty_equals import IsDict
from readyapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="client",
    params=[
        "tutorial001",
        "tutorial001_an",
        pytest.param("tutorial001_an_py39", marks=needs_py39),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.request_forms.{request.param}")

    client = TestClient(mod.app)
    return client


def test_post_body_form(client: TestClient):
    response = client.post("/login/", data={"username": "Foo", "password": "secret"})
    assert response.status_code == 200
    assert response.json() == {"username": "Foo"}


def test_post_body_form_no_password(client: TestClient):
    response = client.post("/login/", data={"username": "Foo"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "password"],
                    "msg": "Field required",
                    "input": None,
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "password"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )


def test_post_body_form_no_username(client: TestClient):
    response = client.post("/login/", data={"password": "secret"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "username"],
                    "msg": "Field required",
                    "input": None,
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "username"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )


def test_post_body_form_no_data(client: TestClient):
    response = client.post("/login/")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "username"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "password"],
                    "msg": "Field required",
                    "input": None,
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "username"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "password"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_post_body_json(client: TestClient):
    response = client.post("/login/", json={"username": "Foo", "password": "secret"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "username"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "password"],
                    "msg": "Field required",
                    "input": None,
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "username"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "password"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/login/": {
                "post": {
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
                    "summary": "Login",
                    "operationId": "login_login__post",
                    "requestBody": {
                        "content": {
                            "application/x-www-form-urlencoded": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_login_login__post"
                                }
                            }
                        },
                        "required": True,
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Body_login_login__post": {
                    "title": "Body_login_login__post",
                    "required": ["username", "password"],
                    "type": "object",
                    "properties": {
                        "username": {"title": "Username", "type": "string"},
                        "password": {"title": "Password", "type": "string"},
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
