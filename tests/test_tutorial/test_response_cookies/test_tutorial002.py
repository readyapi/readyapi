from readyapi.testclient import TestClient

from examples.response_cookies.tutorial002 import app

client = TestClient(app)


def test_path_operation():
    response = client.post("/cookie-and-object/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Come to the dark side, we have cookies"}
    assert response.cookies["fakesession"] == "fake-cookie-session-value"
