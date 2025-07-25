from readyapi.testclient import TestClient

from examples.custom_response.tutorial007 import app

client = TestClient(app)


def test_get():
    fake_content = b"some fake video bytes"
    response = client.get("/")
    assert response.content == fake_content * 10
