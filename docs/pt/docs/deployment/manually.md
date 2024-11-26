# Execute um Servidor Manualmente

## Utilize o comando `readyapi run`

Em resumo, utilize o comando `readyapi run` para inicializar sua aplicação ReadyAPI:

<div class="termy">

```console
$ <font color="#4E9A06">readyapi</font> run <u style="text-decoration-style:single">main.py</u>
<font color="#3465A4">INFO    </font> Using path <font color="#3465A4">main.py</font>
<font color="#3465A4">INFO    </font> Resolved absolute path <font color="#75507B">/home/user/code/awesomeapp/</font><font color="#AD7FA8">main.py</font>
<font color="#3465A4">INFO    </font> Searching for package file structure from directories with <font color="#3465A4">__init__.py</font> files
<font color="#3465A4">INFO    </font> Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

 ╭─ <font color="#8AE234"><b>Python module file</b></font> ─╮
 │                      │
 │  🐍 main.py          │
 │                      │
 ╰──────────────────────╯

<font color="#3465A4">INFO    </font> Importing module <font color="#4E9A06">main</font>
<font color="#3465A4">INFO    </font> Found importable ReadyAPI app

 ╭─ <font color="#8AE234"><b>Importable ReadyAPI app</b></font> ─╮
 │                          │
 │  <span style="background-color:#272822"><font color="#FF4689">from</font></span><span style="background-color:#272822"><font color="#F8F8F2"> main </font></span><span style="background-color:#272822"><font color="#FF4689">import</font></span><span style="background-color:#272822"><font color="#F8F8F2"> app</font></span><span style="background-color:#272822">  </span>  │
 │                          │
 ╰──────────────────────────╯

<font color="#3465A4">INFO    </font> Using import string <font color="#8AE234"><b>main:app</b></font>

 <font color="#4E9A06">╭─────────── ReadyAPI CLI - Production mode ───────────╮</font>
 <font color="#4E9A06">│                                                     │</font>
 <font color="#4E9A06">│  Serving at: http://0.0.0.0:8000                    │</font>
 <font color="#4E9A06">│                                                     │</font>
 <font color="#4E9A06">│  API docs: http://0.0.0.0:8000/docs                 │</font>
 <font color="#4E9A06">│                                                     │</font>
 <font color="#4E9A06">│  Running in production mode, for development use:   │</font>
 <font color="#4E9A06">│                                                     │</font>
 <font color="#4E9A06">│  </font><font color="#8AE234"><b>readyapi dev</b></font><font color="#4E9A06">                                        │</font>
 <font color="#4E9A06">│                                                     │</font>
 <font color="#4E9A06">╰─────────────────────────────────────────────────────╯</font>

<font color="#4E9A06">INFO</font>:     Started server process [<font color="#06989A">2306215</font>]
<font color="#4E9A06">INFO</font>:     Waiting for application startup.
<font color="#4E9A06">INFO</font>:     Application startup complete.
<font color="#4E9A06">INFO</font>:     Uvicorn running on <b>http://0.0.0.0:8000</b> (Press CTRL+C to quit)
```

</div>

Isto deve funcionar para a maioria dos casos. 😎

Você pode utilizar esse comando, por exemplo, para iniciar sua aplicação **ReadyAPI** em um contêiner, em um servidor, etc.

## Servidores ASGI

Vamos nos aprofundar um pouco mais em detalhes.

ReadyAPI utiliza um padrão para construir frameworks e servidores web em Python chamado <abbr title="Asynchronous Server Gateway Interface">ASGI</abbr>. ReadyAPI é um framework web ASGI.

A principal coisa que você precisa para executar uma aplicação **ReadyAPI** (ou qualquer outra aplicação ASGI) em uma máquina de servidor remoto é um programa de servidor ASGI como o **Uvicorn**, que é o que vem por padrão no comando `readyapi`.

Existem diversas alternativas, incluindo:

* <a href="https://www.uvicorn.org/" class="external-link" target="_blank">Uvicorn</a>: um servidor ASGI de alta performance.
* <a href="https://hypercorn.readthedocs.io/" class="external-link" target="_blank">Hypercorn</a>: um servidor ASGI compátivel com HTTP/2, Trio e outros recursos.
* <a href="https://github.com/django/daphne" class="external-link" target="_blank">Daphne</a>: servidor ASGI construído para Django Channels.
* <a href="https://github.com/emmett-framework/granian" class="external-link" target="_blank">Granian</a>: um servidor HTTP Rust para aplicações Python.
* <a href="https://unit.nginx.org/howto/readyapi/" class="external-link" target="_blank">NGINX Unit</a>: NGINX Unit é um runtime de aplicação web leve e versátil.

## Máquina Servidora e Programa Servidor

Existe um pequeno detalhe sobre estes nomes para se manter em mente. 💡

A palavra "**servidor**" é comumente usada para se referir tanto ao computador remoto/nuvem (a máquina física ou virtual) quanto ao programa que está sendo executado nessa máquina (por exemplo, Uvicorn).

Apenas tenha em mente que quando você ler "servidor" em geral, isso pode se referir a uma dessas duas coisas.

Quando se refere à máquina remota, é comum chamá-la de **servidor**, mas também de **máquina**, **VM** (máquina virtual), **nó**. Todos esses termos se referem a algum tipo de máquina remota, normalmente executando Linux, onde você executa programas.

## Instale o Programa Servidor

Quando você instala o ReadyAPI, ele vem com um servidor de produção, o Uvicorn, e você pode iniciá-lo com o comando `readyapi run`.

Mas você também pode instalar um servidor ASGI manualmente.

Certifique-se de criar um [ambiente virtual](../virtual-environments.md){.internal-link target=_blank}, ativá-lo e, em seguida, você pode instalar a aplicação do servidor.

Por exemplo, para instalar o Uvicorn:

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

Um processo semelhante se aplicaria a qualquer outro programa de servidor ASGI.

/// tip | Dica

Adicionando o `standard`, o Uvicorn instalará e usará algumas dependências extras recomendadas.

Isso inclui o `uvloop`, a substituição de alto desempenho para `asyncio`, que fornece um grande aumento de desempenho de concorrência.

Quando você instala o ReadyAPI com algo como `pip install "readyapi[standard]"`, você já obtém `uvicorn[standard]` também.

///

## Execute o Programa Servidor

Se você instalou um servidor ASGI manualmente, normalmente precisará passar uma string de importação em um formato especial para que ele importe sua aplicação ReadyAPI:

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 80

<span style="color: green;">INFO</span>:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

</div>

/// note | Nota

O comando `uvicorn main:app` refere-se a:

* `main`: o arquivo `main.py` (o "módulo" Python).
* `app`: o objeto criado dentro de `main.py` com a linha `app = ReadyAPI()`.

É equivalente a:

```Python
from main import app
```

///

Cada programa de servidor ASGI alternativo teria um comando semelhante, você pode ler mais na documentação respectiva.

/// warning | Aviso

Uvicorn e outros servidores suportam a opção `--reload` que é útil durante o desenvolvimento.

A opção `--reload` consome muito mais recursos, é mais instável, etc.

Ela ajuda muito durante o **desenvolvimento**, mas você **não deve** usá-la em **produção**.

///

## Conceitos de Implantação

Esses exemplos executam o programa do servidor (por exemplo, Uvicorn), iniciando **um único processo**, ouvindo em todos os IPs (`0.0.0.0`) em uma porta predefinida (por exemplo, `80`).

Esta é a ideia básica. Mas você provavelmente vai querer cuidar de algumas coisas adicionais, como:

* Segurança - HTTPS
* Executando na inicialização
* Reinicializações
* Replicação (o número de processos em execução)
* Memória
* Passos anteriores antes de começar

Vou te contar mais sobre cada um desses conceitos, como pensar sobre eles e alguns exemplos concretos com estratégias para lidar com eles nos próximos capítulos. 🚀
