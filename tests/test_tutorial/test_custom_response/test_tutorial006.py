from readyapi.testclient import TestClient

from docs_src.custom_response.tutorial006 import app

client = TestClient(app)


def test_get():
    response = client.get("/cligenius", follow_redirects=False)
    assert response.status_code == 307, response.text
    assert response.headers["location"] == "https://cligenius.khulnasoft.com"


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/cligenius": {
                "get": {
                    "summary": "Redirect Cligenius",
                    "operationId": "redirect_cligenius_cligenius_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            }
        },
    }
