# Middleware

Es gibt mehrere Middlewares, die direkt von Starlette bereitgestellt werden.

Lesen Sie mehr darüber in der [ReadyAPI-Dokumentation über Middleware](../advanced/middleware.md).

::: readyapi.middleware.cors.CORSMiddleware

Kann von `readyapi` importiert werden:

```python
from readyapi.middleware.cors import CORSMiddleware
```

::: readyapi.middleware.gzip.GZipMiddleware

Kann von `readyapi` importiert werden:

```python
from readyapi.middleware.gzip import GZipMiddleware
```

::: readyapi.middleware.httpsredirect.HTTPSRedirectMiddleware

Kann von `readyapi` importiert werden:

```python
from readyapi.middleware.httpsredirect import HTTPSRedirectMiddleware
```

::: readyapi.middleware.trustedhost.TrustedHostMiddleware

Kann von `readyapi` importiert werden:

```python
from readyapi.middleware.trustedhost import TrustedHostMiddleware
```

::: readyapi.middleware.wsgi.WSGIMiddleware

Kann von `readyapi` importiert werden:

```python
from readyapi.middleware.wsgi import WSGIMiddleware
```
