from readyapi.testclient import TestClient

from examples.wsgi.tutorial001 import app

client = TestClient(app)


def test_flask():
    response = client.get("/v1/")
    assert response.status_code == 200, response.text
    assert response.text == "Hello, World from Flask!"


def test_app():
    response = client.get("/v2")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World"}
