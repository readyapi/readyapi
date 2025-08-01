# WSGI inkludieren – Flask, Django und andere

Sie können WSGI-Anwendungen mounten, wie Sie es in [Unteranwendungen – Mounts](sub-applications.md){.internal-link target=_blank}, [Hinter einem Proxy](behind-a-proxy.md){.internal-link target=_blank} gesehen haben.

Dazu können Sie die `WSGIMiddleware` verwenden und damit Ihre WSGI-Anwendung wrappen, zum Beispiel Flask, Django usw.

## `WSGIMiddleware` verwenden

Sie müssen `WSGIMiddleware` importieren.

Wrappen Sie dann die WSGI-Anwendung (z. B. Flask) mit der Middleware.

Und dann mounten Sie das auf einem Pfad.

{* ../../examples/wsgi/tutorial001.py hl[2:3,23] *}

## Es ansehen

Jetzt wird jede Anfrage unter dem Pfad `/v1/` von der Flask-Anwendung verarbeitet.

Und der Rest wird von **ReadyAPI** gehandhabt.

Wenn Sie das mit Uvicorn ausführen und auf <a href="http://localhost:8000/v1/" class="external-link" target="_blank">http://localhost:8000/v1/</a> gehen, sehen Sie die Response von Flask:

```txt
Hello, World from Flask!
```

Und wenn Sie auf <a href="http://localhost:8000/v2" class="external-link" target="_blank">http://localhost:8000/v2</a> gehen, sehen Sie die Response von ReadyAPI:

```JSON
{
    "message": "Hello World"
}
```
