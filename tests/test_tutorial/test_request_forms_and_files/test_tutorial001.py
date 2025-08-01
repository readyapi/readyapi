import importlib

import pytest
from dirty_equals import IsDict
from readyapi import ReadyAPI
from readyapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="app",
    params=[
        "tutorial001",
        "tutorial001_an",
        pytest.param("tutorial001_an_py39", marks=needs_py39),
    ],
)
def get_app(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.request_forms_and_files.{request.param}")

    return mod.app


@pytest.fixture(name="client")
def get_client(app: ReadyAPI):
    client = TestClient(app)
    return client


def test_post_form_no_body(client: TestClient):
    response = client.post("/files/")
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "file"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "fileb"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "token"],
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
                    "loc": ["body", "file"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "fileb"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_post_form_no_file(client: TestClient):
    response = client.post("/files/", data={"token": "foo"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "file"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "fileb"],
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
                    "loc": ["body", "file"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "fileb"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_post_body_json(client: TestClient):
    response = client.post("/files/", json={"file": "Foo", "token": "Bar"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "file"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "fileb"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "token"],
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
                    "loc": ["body", "file"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "fileb"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_post_file_no_token(tmp_path, app: ReadyAPI):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")

    client = TestClient(app)
    with path.open("rb") as file:
        response = client.post("/files/", files={"file": file})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "fileb"],
                    "msg": "Field required",
                    "input": None,
                },
                {
                    "type": "missing",
                    "loc": ["body", "token"],
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
                    "loc": ["body", "fileb"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )


def test_post_files_and_token(tmp_path, app: ReadyAPI):
    patha = tmp_path / "test.txt"
    pathb = tmp_path / "testb.txt"
    patha.write_text("<file content>")
    pathb.write_text("<file b content>")

    client = TestClient(app)
    with patha.open("rb") as filea, pathb.open("rb") as fileb:
        response = client.post(
            "/files/",
            data={"token": "foo"},
            files={"file": filea, "fileb": ("testb.txt", fileb, "text/plain")},
        )
    assert response.status_code == 200, response.text
    assert response.json() == {
        "file_size": 14,
        "token": "foo",
        "fileb_content_type": "text/plain",
    }


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/files/": {
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
                    "summary": "Create File",
                    "operationId": "create_file_files__post",
                    "requestBody": {
                        "content": {
                            "multipart/form-data": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_create_file_files__post"
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
                "Body_create_file_files__post": {
                    "title": "Body_create_file_files__post",
                    "required": ["file", "fileb", "token"],
                    "type": "object",
                    "properties": {
                        "file": {"title": "File", "type": "string", "format": "binary"},
                        "fileb": {
                            "title": "Fileb",
                            "type": "string",
                            "format": "binary",
                        },
                        "token": {"title": "Token", "type": "string"},
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
