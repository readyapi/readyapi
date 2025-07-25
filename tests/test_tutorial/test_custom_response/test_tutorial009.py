from pathlib import Path

from readyapi.testclient import TestClient

from examples.custom_response import tutorial009
from examples.custom_response.tutorial009 import app

client = TestClient(app)


def test_get(tmp_path: Path):
    file_path: Path = tmp_path / "large-video-file.mp4"
    tutorial009.some_file_path = str(file_path)
    test_content = b"Fake video bytes"
    file_path.write_bytes(test_content)
    response = client.get("/")
    assert response.content == test_content
