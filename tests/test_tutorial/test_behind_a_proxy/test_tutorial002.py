from readyapi.testclient import TestClient

from examples.behind_a_proxy.tutorial002 import app

client = TestClient(app)


def test_main():
    response = client.get("/app")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World", "root_path": "/api/v1"}


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/app": {
                "get": {
                    "summary": "Read Main",
                    "operationId": "read_main_app_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            }
        },
        "servers": [{"url": "/api/v1"}],
    }
