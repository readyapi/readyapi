# WebSockets

When defining WebSockets, you normally declare a parameter of type `WebSocket` and with it you can read data from the client and send data to it.

It is provided directly by Starlette, but you can import it from `readyapi`:

```python
from readyapi import WebSocket
```

/// tip

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

///

::: readyapi.WebSocket
options:
members: - scope - app - url - base_url - headers - query_params - path_params - cookies - client - state - url_for - client_state - application_state - receive - send - accept - receive_text - receive_bytes - receive_json - iter_text - iter_bytes - iter_json - send_text - send_bytes - send_json - close

When a client disconnects, a `WebSocketDisconnect` exception is raised, you can catch it.

You can import it directly form `readyapi`:

```python
from readyapi import WebSocketDisconnect
```

::: readyapi.WebSocketDisconnect

## WebSockets - additional classes

Additional classes for handling WebSockets.

Provided directly by Starlette, but you can import it from `readyapi`:

```python
from readyapi.websockets import WebSocketDisconnect, WebSocketState
```

::: readyapi.websockets.WebSocketDisconnect

::: readyapi.websockets.WebSocketState
