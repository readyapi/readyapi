import pytest
from readyapi import ReadyAPI, Query, Path, Header, Cookie, Body, Form, File
from readyapi.testclient import TestClient


app = ReadyAPI()


@app.get("/items/")
async def read_items(
    q: str = Query(default=None),
    p: str = Path(default="default_path"),
    h: str = Header(default="default_header"),
    c: str = Cookie(default="default_cookie"),
):
    return {"q": q, "p": p, "h": h, "c": c}


@app.post("/items/")
async def create_item(
    item: dict = Body(...),
    form: dict = Form(...),
    file: bytes = File(...),
):
    return {"item": item, "form": form, "file": file}


client = TestClient(app)


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "q": None,
        "p": "default_path",
        "h": "default_header",
        "c": "default_cookie",
    }


def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "item1"},
        data={"form_field": "form_value"},
        files={"file": ("filename.txt", b"file content")},
    )
    assert response.status_code == 200
    assert response.json() == {
        "item": {"name": "item1"},
        "form": {"form_field": "form_value"},
        "file": "file content",
    }


def test_read_items_with_query():
    response = client.get("/items/?q=query_value")
    assert response.status_code == 200
    assert response.json() == {
        "q": "query_value",
        "p": "default_path",
        "h": "default_header",
        "c": "default_cookie",
    }


def test_read_items_with_path():
    response = client.get("/items/default_path")
    assert response.status_code == 200
    assert response.json() == {
        "q": None,
        "p": "default_path",
        "h": "default_header",
        "c": "default_cookie",
    }


def test_read_items_with_header():
    response = client.get("/items/", headers={"h": "header_value"})
    assert response.status_code == 200
    assert response.json() == {
        "q": None,
        "p": "default_path",
        "h": "header_value",
        "c": "default_cookie",
    }


def test_read_items_with_cookie():
    client.cookies.set("c", "cookie_value")
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "q": None,
        "p": "default_path",
        "h": "default_header",
        "c": "cookie_value",
    }
