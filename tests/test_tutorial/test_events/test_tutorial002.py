import pytest
from readyapi import ReadyAPI
from readyapi.testclient import TestClient


@pytest.fixture(name="app", scope="module")
def get_app():
    with pytest.warns(DeprecationWarning):
        from examples.events.tutorial002 import app
    yield app


def test_events(app: ReadyAPI):
    with TestClient(app) as client:
        response = client.get("/items/")
        assert response.status_code == 200, response.text
        assert response.json() == [{"name": "Foo"}]
    with open("log.txt") as log:
        assert "Application shutdown" in log.read()


def test_openapi_schema(app: ReadyAPI):
    with TestClient(app) as client:
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
                        "summary": "Read Items",
                        "operationId": "read_items_items__get",
                    }
                }
            },
        }
