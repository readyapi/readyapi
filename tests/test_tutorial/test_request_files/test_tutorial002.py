import importlib

import pytest
from dirty_equals import IsDict
from readyapi import ReadyAPI
from readyapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="app",
    params=[
        "tutorial002",
        "tutorial002_an",
        pytest.param("tutorial002_py39", marks=needs_py39),
        pytest.param("tutorial002_an_py39", marks=needs_py39),
    ],
)
def get_app(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.request_files.{request.param}")

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
                    "loc": ["body", "files"],
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
                    "loc": ["body", "files"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )


def test_post_body_json(client: TestClient):
    response = client.post("/files/", json={"file": "Foo"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "files"],
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
                    "loc": ["body", "files"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )


def test_post_files(tmp_path, app: ReadyAPI):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")
    path2 = tmp_path / "test2.txt"
    path2.write_bytes(b"<file content2>")

    client = TestClient(app)
    with path.open("rb") as file, path2.open("rb") as file2:
        response = client.post(
            "/files/",
            files=(
                ("files", ("test.txt", file)),
                ("files", ("test2.txt", file2)),
            ),
        )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_sizes": [14, 15]}


def test_post_upload_file(tmp_path, app: ReadyAPI):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")
    path2 = tmp_path / "test2.txt"
    path2.write_bytes(b"<file content2>")

    client = TestClient(app)
    with path.open("rb") as file, path2.open("rb") as file2:
        response = client.post(
            "/uploadfiles/",
            files=(
                ("files", ("test.txt", file)),
                ("files", ("test2.txt", file2)),
            ),
        )
    assert response.status_code == 200, response.text
    assert response.json() == {"filenames": ["test.txt", "test2.txt"]}


def test_get_root(app: ReadyAPI):
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert b"<form" in response.content


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
                    "summary": "Create Files",
                    "operationId": "create_files_files__post",
                    "requestBody": {
                        "content": {
                            "multipart/form-data": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_create_files_files__post"
                                }
                            }
                        },
                        "required": True,
                    },
                }
            },
            "/uploadfiles/": {
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
                    "summary": "Create Upload Files",
                    "operationId": "create_upload_files_uploadfiles__post",
                    "requestBody": {
                        "content": {
                            "multipart/form-data": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_create_upload_files_uploadfiles__post"
                                }
                            }
                        },
                        "required": True,
                    },
                }
            },
            "/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Main",
                    "operationId": "main__get",
                }
            },
        },
        "components": {
            "schemas": {
                "Body_create_upload_files_uploadfiles__post": {
                    "title": "Body_create_upload_files_uploadfiles__post",
                    "required": ["files"],
                    "type": "object",
                    "properties": {
                        "files": {
                            "title": "Files",
                            "type": "array",
                            "items": {"type": "string", "format": "binary"},
                        }
                    },
                },
                "Body_create_files_files__post": {
                    "title": "Body_create_files_files__post",
                    "required": ["files"],
                    "type": "object",
                    "properties": {
                        "files": {
                            "title": "Files",
                            "type": "array",
                            "items": {"type": "string", "format": "binary"},
                        }
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
