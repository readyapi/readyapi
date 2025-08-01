from readyapi.testclient import TestClient

from examples.advanced_middleware.tutorial001 import app


def test_middleware():
    client = TestClient(app, base_url="https://testserver")
    response = client.get("/")
    assert response.status_code == 200, response.text

    client = TestClient(app)
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307, response.text
    assert response.headers["location"] == "https://testserver/"
