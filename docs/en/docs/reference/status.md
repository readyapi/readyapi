# Status Codes

You can import the `status` module from `readyapi`:

```python
from readyapi import status
```

`status` is provided directly by Starlette.

It contains a group of named constants (variables) with integer status codes.

For example:

* 200: `status.HTTP_200_OK`
* 403: `status.HTTP_403_FORBIDDEN`
* etc.

It can be convenient to quickly access HTTP (and WebSocket) status codes in your app, using autocompletion for the name without having to remember the integer status codes by memory.

Read more about it in the [ReadyAPI docs about Response Status Code](https://readyapi.github.io/tutorial/response-status-code/).

## Example

```python
from readyapi import ReadyAPI, status

app = ReadyAPI()


@app.get("/items/", status_code=status.HTTP_418_IM_A_TEAPOT)
def read_items():
    return [{"name": "Plumbus"}, {"name": "Portal Gun"}]
```

::: readyapi.status
