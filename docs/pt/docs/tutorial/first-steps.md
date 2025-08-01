# Primeiros Passos

O arquivo ReadyAPI mais simples pode se parecer com:

{* ../../examples/first_steps/tutorial001.py *}

Copie o conteúdo para um arquivo `main.py`.

Execute o servidor:

<div class="termy">

```console
$ <font color="#4E9A06">readyapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> ReadyAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the ReadyAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>readyapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

Na saída, temos:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Essa linha mostra a URL onde a sua aplicação está sendo servida, que nesse caso é a sua máquina local.

### Confira

Abra o seu navegador em <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a>.

Você verá essa resposta em JSON:

```JSON
{"message": "Hello World"}
```

### Documentação Interativa de APIs

Agora vá para <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Você verá a documentação interativa automática da API (fornecida por <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Documentação Alternativa de APIs

E agora, vá para <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Você verá a documentação alternativa automática (fornecida por <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

### OpenAPI

O **ReadyAPI** gera um "*schema*" com toda a sua API usando o padrão **OpenAPI** para definir APIs.

#### "*Schema*"

Um "*schema*" é uma definição ou descrição de algo. Não o código que o implementa, mas apenas uma descrição abstrata.

#### API "*schema*"

Nesse caso, <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> é uma especificação que determina como definir um *schema* da sua API.

Esta definição de *schema* inclui as rotas da sua API, os parâmetros possíveis que elas usam, etc.

#### "*Schema*" de dados

O termo "*schema*" também pode se referir à forma de alguns dados, como um conteúdo JSON.

Nesse caso, significaria os atributos JSON e os tipos de dados que eles possuem, etc.

#### OpenAPI e JSON *Schema*

OpenAPI define um *schema* de API para sua API. E esse *schema* inclui definições (ou "*schemas*") dos dados enviados e recebidos por sua API usando **JSON *Schema***, o padrão para *schemas* de dados JSON.

#### Verifique o `openapi.json`

Se você está curioso(a) sobre a aparência do *schema* bruto OpenAPI, o ReadyAPI gera automaticamente um JSON (*schema*) com as descrições de toda a sua API.

Você pode ver isso diretamente em: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a>.

Ele mostrará um JSON começando com algo como:

```JSON
{
    "openapi": "3.0.2",
    "info": {
        "title": "ReadyAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
```

#### Para que serve o OpenAPI

O *schema* OpenAPI é o que possibilita os dois sistemas de documentação interativos mostrados.

E existem dezenas de alternativas, todas baseadas em OpenAPI. Você pode facilmente adicionar qualquer uma dessas alternativas à sua aplicação criada com **ReadyAPI**.

Você também pode usá-lo para gerar código automaticamente para clientes que se comunicam com sua API. Por exemplo, aplicativos front-end, móveis ou IoT.

## Recapitulando, passo a passo

### Passo 1: importe `ReadyAPI`

{* ../../examples/first_steps/tutorial001.py hl[1] *}

`ReadyAPI` é uma classe Python que fornece todas as funcionalidades para sua API.

/// note | Detalhes técnicos

`ReadyAPI` é uma classe que herda diretamente de `Starlette`.

Você pode usar todas as funcionalidades do <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> com `ReadyAPI` também.

///

### Passo 2: crie uma "instância" de `ReadyAPI`

{* ../../examples/first_steps/tutorial001.py hl[3] *}

Aqui, a variável `app` será uma "instância" da classe `ReadyAPI`.

Este será o principal ponto de interação para criar toda a sua API.

### Passo 3: crie uma *rota*

#### Rota

"Rota" aqui se refere à última parte da URL, começando do primeiro `/`.

Então, em uma URL como:

```
https://example.com/items/foo
```

...a rota seria:

```
/items/foo
```

/// info | Informação

Uma "rota" também é comumente chamada de "endpoint".

///

Ao construir uma API, a "rota" é a principal forma de separar "preocupações" e "recursos".

#### Operação

"Operação" aqui se refere a um dos "métodos" HTTP.

Um dos:

* `POST`
* `GET`
* `PUT`
* `DELETE`

...e os mais exóticos:

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

No protocolo HTTP, você pode se comunicar com cada rota usando um (ou mais) desses "métodos".

---

Ao construir APIs, você normalmente usa esses métodos HTTP para executar uma ação específica.

Normalmente você usa:

* `POST`: para criar dados.
* `GET`: para ler dados.
* `PUT`: para atualizar dados.
* `DELETE`: para deletar dados.

Portanto, no OpenAPI, cada um dos métodos HTTP é chamado de "operação".

Vamos chamá-los de "**operações**" também.

#### Defina um *decorador de rota*

{* ../../examples/first_steps/tutorial001.py hl[6] *}

O `@app.get("/")` diz ao **ReadyAPI** que a função logo abaixo é responsável por tratar as requisições que vão para:

* a rota `/`
* usando o  <abbr title="o método HTTP GET">operador <code>get</code></abbr>

/// info | `@decorador`

Essa sintaxe `@alguma_coisa` em Python é chamada de "decorador".

Você o coloca em cima de uma função. Como um chapéu decorativo (acho que é daí que vem o termo).

Um "decorador" pega a função abaixo e faz algo com ela.

Em nosso caso, este decorador informa ao **ReadyAPI** que a função abaixo corresponde a **rota** `/` com uma **operação** `get`.

É o "**decorador de rota**".

///

Você também pode usar as outras operações:

* `@app.post()`
* `@app.put()`
* `@app.delete()`

E os mais exóticos:

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

/// tip | Dica

Você está livre para usar cada operação (método HTTP) como desejar.

O **ReadyAPI** não impõe nenhum significado específico.

As informações aqui são apresentadas como uma orientação, não uma exigência.

Por exemplo, ao usar GraphQL, você normalmente executa todas as ações usando apenas operações `POST`.

///

### Passo 4: defina uma **função de rota**

Esta é a nossa "**função de rota**":

* **rota**: é `/`.
* **operação**: é `get`.
* **função**: é a função abaixo do "decorador" (abaixo do `@app.get("/")`).

{* ../../examples/first_steps/tutorial001.py hl[7] *}

Esta é uma função Python.

Ela será chamada pelo **ReadyAPI** sempre que receber uma requisição para a URL "`/ `" usando uma operação `GET`.

Neste caso, é uma função `assíncrona`.

---

Você também pode defini-la como uma função normal em vez de `async def`:

{* ../../examples/first_steps/tutorial003.py hl[7] *}

/// note | Nota

Se você não sabe a diferença, verifique o [Async: *"Com pressa?"*](../async.md#com-pressa){.internal-link target=_blank}.

///

### Passo 5: retorne o conteúdo

{* ../../examples/first_steps/tutorial001.py hl[8] *}

Você pode retornar um `dict`, `list` e valores singulares como `str`, `int`, etc.

Você também pode devolver modelos Pydantic (você verá mais sobre isso mais tarde).

Existem muitos outros objetos e modelos que serão convertidos automaticamente para JSON (incluindo ORMs, etc). Tente usar seus favoritos, é altamente provável que já sejam compatíveis.

## Recapitulando

* Importe `ReadyAPI`.
* Crie uma instância do `app`.
* Coloque o **decorador que define a operação** (como `@app.get("/")`).
* Escreva uma **função para a operação da rota** (como `def root(): ...`) abaixo.
* Execute o servidor de desenvolvimento (como `uvicorn main:app --reload`).
