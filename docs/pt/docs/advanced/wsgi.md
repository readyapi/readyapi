# Adicionando WSGI - Flask, Django, entre outros

Como você viu em [Sub Applications - Mounts](sub-applications.md){.internal-link target=_blank} e [Behind a Proxy](behind-a-proxy.md){.internal-link target=_blank}, você pode **"montar"** aplicações WSGI.

Para isso, você pode utilizar o `WSGIMiddleware` para encapsular a sua aplicação WSGI, como por exemplo Flask, Django, etc.

## Usando o `WSGIMiddleware`

Você precisa importar o `WSGIMiddleware`.

Em seguinda, encapsular a aplicação WSGI (e.g. Flask) com o middleware.

E então **"montar"** em um caminho de rota.

{* ../../examples/wsgi/tutorial001.py hl[2:3,23] *}

## Conferindo

Agora todas as requisições sob o caminho `/v1/` serão manipuladas pela aplicação utilizando Flask.

E o resto será manipulado pelo **ReadyAPI**.

Se você rodar a aplicação e ir até <a href="http://localhost:8000/v1/" class="external-link" target="_blank">http://localhost:8000/v1/</a>, você verá o retorno do Flask:

```txt
Hello, World from Flask!
```

E se você for até <a href="http://localhost:8000/v2" class="external-link" target="_blank">http://localhost:8000/v2</a>, você verá o retorno do ReadyAPI:

```JSON
{
    "message": "Hello World"
}
```
