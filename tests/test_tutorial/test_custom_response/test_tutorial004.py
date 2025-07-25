from readyapi.testclient import TestClient

from examples.custom_response.tutorial004 import app

client = TestClient(app)


html_contents = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


def test_get_custom_response():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.text == html_contents


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"text/html": {"schema": {"type": "string"}}},
                        }
                    },
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                }
            }
        },
    }
