from readyapi.testclient import TestClient

from docs_src.custom_response.tutorial006b import app

client = TestClient(app)


def test_redirect_response_class():
    response = client.get("/readyapi", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://readyapi.khulnasoft.com"


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/readyapi": {
                "get": {
                    "summary": "Redirect Readyapi",
                    "operationId": "redirect_readyapi_readyapi_get",
                    "responses": {"307": {"description": "Successful Response"}},
                }
            }
        },
    }
