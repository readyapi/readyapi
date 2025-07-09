from readyapi.testclient import TestClient

from examples.custom_response.tutorial009c import app

client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.content == b'{\n  "message": "Hello World"\n}'
