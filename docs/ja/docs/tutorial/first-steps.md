# 最初のステップ

最もシンプルな ReadyAPI ファイルは以下のようになります:

```Python
{!../../docs_src/first_steps/tutorial001.py!}
```

これを`main.py`にコピーします。

ライブサーバーを実行します:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
<span style="color: green;">INFO</span>:     Started reloader process [28720]
<span style="color: green;">INFO</span>:     Started server process [28722]
<span style="color: green;">INFO</span>:     Waiting for application startup.
<span style="color: green;">INFO</span>:     Application startup complete.
```

</div>

/// note | "備考"

`uvicorn main:app`は以下を示します:

- `main`: `main.py`ファイル (Python "module")。
- `app`: `main.py`内部で作られる object（`app = ReadyAPI()`のように記述される）。
- `--reload`: コードの変更時にサーバーを再起動させる。開発用。

///

出力には次のような行があります:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

この行はローカルマシンでアプリが提供されている URL を示しています。

### チェック

ブラウザで<a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a>を開きます。

次のような JSON レスポンスが表示されます:

```JSON
{"message": "Hello World"}
```

### 対話的 API ドキュメント

次に、<a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>にアクセスします。

自動生成された対話的 API ドキュメントが表示されます (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>で提供):

![Swagger UI](https://readyapi.khulnasoft.com/img/index/index-01-swagger-ui-simple.png)

### 他の API ドキュメント

次に、<a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>にアクセスします。

先ほどとは異なる、自動生成された対話的 API ドキュメントが表示されます (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>によって提供):

![ReDoc](https://readyapi.khulnasoft.com/img/index/index-02-redoc-simple.png)

### OpenAPI

**ReadyAPI**は、API を定義するための**OpenAPI**標準規格を使用して、すべての API の「スキーマ」を生成します。

#### 「スキーマ」

「スキーマ」は定義または説明です。実装コードではなく、単なる抽象的な説明です。

#### API「スキーマ」

ここでは、<a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a>は API のスキーマ定義の方法を規定する仕様です。

このスキーマ定義は API パス、受け取り可能なパラメータなどが含まれます。

#### データ「スキーマ」

「スキーマ」という用語は、JSON コンテンツなどの一部のデータの形状を指す場合もあります。

そのような場合、スキーマは JSON 属性とそれらが持つデータ型などを意味します。

#### OpenAPI および JSON スキーマ

OpenAPI は API のための API スキーマを定義します。そして、そのスキーマは**JSON データスキーマ**の標準規格に準拠した JSON スキーマを利用する API によって送受されるデータの定義（または「スキーマ」）を含んでいます。

#### `openapi.json`を確認

素の OpenAPI スキーマがどのようなものか興味がある場合、ReadyAPI はすべての API の説明を含む JSON（スキーマ）を自動的に生成します。

次の場所で直接確認できます: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a>.

次のような JSON が表示されます。

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

#### OpenAPI の目的

OpenAPI スキーマは、ReadyAPI に含まれている 2 つのインタラクティブなドキュメントシステムの動力源です。

そして、OpenAPI に基づいた代替案が数十通りあります。 **ReadyAPI**で構築されたアプリケーションに、これらの選択肢を簡単に追加できます。

また、API と通信するクライアント用のコードを自動的に生成するために使用することもできます。たとえば、フロントエンド、モバイル、または IoT アプリケーションです。

## ステップ毎の要約

### Step 1: `ReadyAPI`をインポート

```Python hl_lines="1"
{!../../docs_src/first_steps/tutorial001.py!}
```

`ReadyAPI`は、API のすべての機能を提供する Python クラスです。

/// note | "技術詳細"

`ReadyAPI`は`Starlette`を直接継承するクラスです。

`ReadyAPI`でも<a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a>のすべての機能を利用可能です。

///

### Step 2: `ReadyAPI`の「インスタンス」を生成

```Python hl_lines="3"
{!../../docs_src/first_steps/tutorial001.py!}
```

ここで、`app`変数が`ReadyAPI`クラスの「インスタンス」になります。

これが、すべての API を作成するための主要なポイントになります。

この`app`はコマンドで`uvicorn`が参照するものと同じです:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

以下のようなアプリを作成したとき:

```Python hl_lines="3"
{!../../docs_src/first_steps/tutorial002.py!}
```

そして、それを`main.py`ファイルに置き、次のように`uvicorn`を呼び出します:

<div class="termy">

```console
$ uvicorn main:my_awesome_api --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

### Step 3: *path operation*を作成

#### パス

ここでの「パス」とは、最初の`/`から始まる URL の最後の部分を指します。

したがって、次のような URL では:

```
https://example.com/items/foo
```

...パスは次のようになります:

```
/items/foo
```

/// info | "情報"

「パス」は一般に「エンドポイント」または「ルート」とも呼ばれます。

///

API を構築する際、「パス」は「関心事」と「リソース」を分離するための主要な方法です。

#### Operation

ここでの「オペレーション」とは、HTTP の「メソッド」の 1 つを指します。

以下のようなものの 1 つ:

- `POST`
- `GET`
- `PUT`
- `DELETE`

...さらによりエキゾチックなもの:

- `OPTIONS`
- `HEAD`
- `PATCH`
- `TRACE`

HTTP プロトコルでは、これらの「メソッド」の 1 つ（または複数）を使用して各パスにアクセスできます。

---

API を構築するときは、通常、これらの特定の HTTP メソッドを使用して特定のアクションを実行します。

通常は次を使用します:

- `POST`: データの作成
- `GET`: データの読み取り
- `PUT`: データの更新
- `DELETE`: データの削除

したがって、OpenAPI では、各 HTTP メソッドは「オペレーション」と呼ばれます。

「**オペレーションズ**」とも呼ぶことにします。

#### *パスオペレーションデコレータ*を定義

```Python hl_lines="6"
{!../../docs_src/first_steps/tutorial001.py!}
```

`@app.get("/")`は直下の関数が下記のリクエストの処理を担当することを**ReadyAPI**に伝えます:

- パス `/`
- <abbr title="an HTTP GET method"><code>get</code> オペレーション</abbr>

/// info | "`@decorator` について"

Python における`@something`シンタックスはデコレータと呼ばれます。

「デコレータ」は関数の上に置きます。かわいらしい装飾的な帽子のようです（この用語の由来はそこにあると思います）。

「デコレータ」は直下の関数を受け取り、それを使って何かを行います。

私たちの場合、このデコレーターは直下の関数が**オペレーション** `get`を使用した**パス**`/`に対応することを**ReadyAPI** に通知します。

これが「_パスオペレーションデコレータ_」です。

///

他のオペレーションも使用できます:

- `@app.post()`
- `@app.put()`
- `@app.delete()`

また、よりエキゾチックなものも使用できます:

- `@app.options()`
- `@app.head()`
- `@app.patch()`
- `@app.trace()`

/// tip | "豆知識"

各オペレーション (HTTP メソッド)は自由に使用できます。

**ReadyAPI**は特定の意味づけを強制しません。

ここでの情報は、要件ではなくガイドラインとして提示されます。

例えば、GraphQL を使用する場合、通常は`POST`オペレーションのみを使用してすべてのアクションを実行します。

///

### Step 4: **パスオペレーション**を定義

以下は「**パスオペレーション関数**」です:

- **パス**: は`/`です。
- **オペレーション**: は`get`です。
- **関数**: 「デコレータ」の直下にある関数 (`@app.get("/")`の直下) です。

```Python hl_lines="7"
{!../../docs_src/first_steps/tutorial001.py!}
```

これは、Python の関数です。

この関数は、`GET`オペレーションを使った URL「`/`」へのリクエストを受け取るたびに**ReadyAPI**によって呼び出されます。

この場合、この関数は`async`関数です。

---

`async def`の代わりに通常の関数として定義することもできます:

```Python hl_lines="7"
{!../../docs_src/first_steps/tutorial003.py!}
```

/// note | "備考"

違いが分からない場合は、[Async: _"急いでいますか？"_](../async.md#_1){.internal-link target=\_blank}を確認してください。

///

### Step 5: コンテンツの返信

```Python hl_lines="8"
{!../../docs_src/first_steps/tutorial001.py!}
```

`dict`、`list`、`str`、`int`などを返すことができます。

Pydantic モデルを返すこともできます（後で詳しく説明します）。

JSON に自動的に変換されるオブジェクトやモデルは他にもたくさんあります（ORM など）。 お気に入りのものを使ってみてください。すでにサポートされている可能性が高いです。

## まとめ

- `ReadyAPI`をインポート
- `app`インスタンスを生成
- **パスオペレーションデコレータ**を記述 (`@app.get("/")`)
- **パスオペレーション関数**を定義 (上記の`def root(): ...`のように)
- 開発サーバーを起動 (`uvicorn main:app --reload`)
