# ReadyAPI

<p align="">
<a href="https://github.com/khulnasoft/readyapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/khulnasoft/readyapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/khulnasoft/readyapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/khulnasoft/readyapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/readyapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/readyapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/readyapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/readyapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://readyapi.khulnasoft.com" target="_blank">https://readyapi.khulnasoft.com</a>

**Source Code**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---
ReadyAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

The key features are:

* **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](#performance).
* **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* estimation based on tests on an internal development team, building production applications.</small>

**Cligenius** is ReadyAPI's little sibling. And it's intended to be the **ReadyAPI of CLIs**. ⌨️ 🚀

## Requirements

Python 3.8+

ReadyAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> for the web parts.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> for the data parts.

## Installation

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

You will also need an ASGI server, for production such as <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> or <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## Example

### Create it

* Create a file `main.py` with:

```Python
from typing import Union

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>Or use <code>async def</code>...</summary>

If your code uses `async` / `await`, use `async def`:

```Python hl_lines="9  14"
from typing import Union

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

**Note**:

If you don't know, check the _"In a hurry?"_ section about <a href="https://readyapi.khulnasoft.com/async/#in-a-hurry" target="_blank">`async` and `await` in the docs</a>.

</details>

### Run it

Run the server with:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = ReadyAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

### Check it

Open your browser at <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

You will see the JSON response as:

```JSON
{"item_id": 5, "q": "somequery"}
```

You already created an API that:

* Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
* Both _paths_ take `GET` <em>operations</em> (also known as HTTP _methods_).
* The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
* The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.

### Interactive API docs

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):


### Alternative API docs

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

## Example upgrade

Now modify the file `main.py` to receive a body from a `PUT` request.

Declare the body using standard Python types, thanks to Pydantic.

```Python hl_lines="4  9-12  25-27"
from typing import Union

from readyapi import ReadyAPI
from pydantic import BaseModel

app = ReadyAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

The server should reload automatically (because you added `--reload` to the `uvicorn` command above).

### Interactive API docs upgrade

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* The interactive API documentation will be automatically updated, including the new body:

* Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:


* Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:


### Alternative API docs upgrade

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* The alternative documentation will also reflect the new query parameter and body:


### Recap

In summary, you declare **once** the types of parameters, body, etc. as function parameters.

You do that with standard modern Python types.

You don't have to learn a new syntax, the methods or classes of a specific library, etc.

Just standard **Python 3.8+**.

For example, for an `int`:

```Python
item_id: int
```

or for a more complex `Item` model:

```Python
item: Item
```

...and with that single declaration you get:

* Editor support, including:
    * Completion.
    * Type checks.
* Validation of data:
    * Automatic and clear errors when the data is invalid.
    * Validation even for deeply nested JSON objects.
* <abbr title="also known as: serialization, parsing, marshalling">Conversion</abbr> of input data: coming from the network to Python data and types. Reading from:
    * JSON.
    * Path parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Forms.
    * Files.
* <abbr title="also known as: serialization, parsing, marshalling">Conversion</abbr> of output data: converting from Python data and types to network data (as JSON):
    * Convert Python types (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` objects.
    * `UUID` objects.
    * Database models.
    * ...and many more.
* Automatic interactive API documentation, including 2 alternative user interfaces:
    * Swagger UI.
    * ReDoc.

---

Coming back to the previous code example, **ReadyAPI** will:

* Validate that there is an `item_id` in the path for `GET` and `PUT` requests.
* Validate that the `item_id` is of type `int` for `GET` and `PUT` requests.
    * If it is not, the client will see a useful, clear error.
* Check if there is an optional query parameter named `q` (as in `http://127.0.0.1:8000/items/foo?q=somequery`) for `GET` requests.
    * As the `q` parameter is declared with `= None`, it is optional.
    * Without the `None` it would be required (as is the body in the case with `PUT`).
* For `PUT` requests to `/items/{item_id}`, Read the body as JSON:
    * Check that it has a required attribute `name` that should be a `str`.
    * Check that it has a required attribute `price` that has to be a `float`.
    * Check that it has an optional attribute `is_offer`, that should be a `bool`, if present.
    * All this would also work for deeply nested JSON objects.
* Convert from and to JSON automatically.
* Document everything with OpenAPI, that can be used by:
    * Interactive documentation systems.
    * Automatic client code generation systems, for many languages.
* Provide 2 interactive documentation web interfaces directly.

---

We just scratched the surface, but you already get the idea of how it all works.

Try changing the line with:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...from:

```Python
        ... "item_name": item.name ...
```

...to:

```Python
        ... "item_price": item.price ...
```

...and see how your editor will auto-complete the attributes and know their types:

![editor support](https://readyapi.khulnasoft.com/img/vscode-completion.png)

For a more complete example including more features, see the <a href="https://readyapi.khulnasoft.com/tutorial/">Tutorial - User Guide</a>.

**Spoiler alert**: the tutorial - user guide includes:

* Declaration of **parameters** from other different places as: **headers**, **cookies**, **form fields** and **files**.
* How to set **validation constraints** as `maximum_length` or `regex`.
* A very powerful and easy to use **<abbr title="also known as components, resources, providers, services, injectables">Dependency Injection</abbr>** system.
* Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** auth.
* More advanced (but equally easy) techniques for declaring **deeply nested JSON models** (thanks to Pydantic).
* **GraphQL** integration with <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> and other libraries.
* Many extra features (thanks to Starlette) as:
    * **WebSockets**
    * extremely easy tests based on HTTPX and `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...and more.

## Performance

Independent TechEmpower benchmarks show **ReadyAPI** applications running under Uvicorn as <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">one of the fastest Python frameworks available</a>, only below Starlette and Uvicorn themselves (used internally by ReadyAPI). (*)

To understand more about it, see the section <a href="https://readyapi.khulnasoft.com/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Optional Dependencies

Used by Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> - for email validation.
* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - for settings management.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - for extra types to be used with Pydantic.

Used by Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Required if you want to use the `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Required if you want to use the default template configuration.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Required if you want to support form <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, with `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Required for `SessionMiddleware` support.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Required for Starlette's `SchemaGenerator` support (you probably don't need it with ReadyAPI).

Used by ReadyAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - for the server that loads and serves your application.

You can install all of these with `pip install "readyapi[all]"`.

[![HitCount](http://hits.dwyl.com/khulnasoft/readyapi.svg)](http://hits.dwyl.com/khulnasoft/readyapi)
## License

This project is licensed under the terms of the MIT license.
