import importlib

import pytest
from readyapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="client",
    params=[
        "tutorial005",
        pytest.param("tutorial005_py39", marks=needs_py39),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"examples.extra_models.{request.param}")

    client = TestClient(mod.app)
    return client


def test_get_items(client: TestClient):
    response = client.get("/keyword-weights/")
    assert response.status_code == 200, response.text
    assert response.json() == {"foo": 2.3, "bar": 3.4}


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/keyword-weights/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Read Keyword Weights Keyword Weights  Get",
                                        "type": "object",
                                        "additionalProperties": {"type": "number"},
                                    }
                                }
                            },
                        }
                    },
                    "summary": "Read Keyword Weights",
                    "operationId": "read_keyword_weights_keyword_weights__get",
                }
            }
        },
    }
