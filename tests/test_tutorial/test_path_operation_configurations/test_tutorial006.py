import pytest
from readyapi.testclient import TestClient

from examples.path_operation_configuration.tutorial006 import app

client = TestClient(app)


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/items/", 200, [{"name": "Foo", "price": 42}]),
        ("/users/", 200, [{"username": "johndoe"}]),
        ("/elements/", 200, [{"item_id": "Foo"}]),
    ],
)
def test_query_params_str_validations(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response


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
                    "tags": ["items"],
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                }
            },
            "/users/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "tags": ["users"],
                    "summary": "Read Users",
                    "operationId": "read_users_users__get",
                }
            },
            "/elements/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "tags": ["items"],
                    "summary": "Read Elements",
                    "operationId": "read_elements_elements__get",
                    "deprecated": True,
                }
            },
        },
    }
