from pytest import MonkeyPatch
from readyapi.testclient import TestClient

from ...utils import needs_pydanticv2


@needs_pydanticv2
def test_settings(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("ADMIN_EMAIL", "admin@example.com")
    from examples.settings.tutorial001 import app

    client = TestClient(app)
    response = client.get("/info")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "app_name": "Awesome API",
        "admin_email": "admin@example.com",
        "items_per_user": 50,
    }
