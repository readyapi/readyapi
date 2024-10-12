# 条件付き OpenAPI

必要であれば、設定と環境変数を利用して、環境に応じて条件付きで OpenAPI を構成することが可能です。また、完全に OpenAPI を無効にすることもできます。

## セキュリティと API、およびドキュメントについて

本番環境においてドキュメントの UI を非表示にすることによって、API を保護しようと _すべきではありません_。

それは、API のセキュリティの強化にはならず、_path operations_ は依然として利用可能です。

もしセキュリティ上の欠陥がソースコードにあるならば、それは存在したままです。

ドキュメンテーションを非表示にするのは、単にあなたの API へのアクセス方法を難解にするだけでなく、同時にあなた自身の本番環境での API のデバッグを困難にしてしまう可能性があります。単純に、 <a href="https://en.wikipedia.org/wiki/Security_through_obscurity" class="external-link" target="_blank">Security through obscurity</a> の一つの形態として考えられるでしょう。

もしあなたの API のセキュリティを強化したいなら、いくつかのよりよい方法があります。例を示すと、

- リクエストボディとレスポンスのための Pydantic モデルの定義を見直す。
- 依存関係に基づきすべての必要なパーミッションとロールを設定する。
- パスワードを絶対に平文で保存しない。パスワードハッシュのみを保存する。
- Passlib や JWT トークンに代表される、よく知られた暗号化ツールを使って実装する。
- そして必要なところでは、もっと細かいパーミッション制御を OAuth2 スコープを使って行う。
- など

それでも、例えば本番環境のような特定の環境のみで、あるいは環境変数の設定によって API ドキュメントをどうしても無効にしたいという、非常に特殊なユースケースがあるかもしれません。

## 設定と環境変数による条件付き OpenAPI

生成する OpenAPI とドキュメント UI の構成は、共通の Pydantic の設定を使用して簡単に切り替えられます。

例えば、

```Python hl_lines="6  11"
{!../../docs_src/conditional_openapi/tutorial001.py!}
```

ここでは `openapi_url` の設定を、デフォルトの `"/openapi.json"` のまま宣言しています。

そして、これを `ReadyAPI` app を作る際に使います。

それから、以下のように `OPENAPI_URL` という環境変数を空文字列に設定することによって OpenAPI (UI ドキュメントを含む) を無効化することができます。

<div class="termy">

```console
$ OPENAPI_URL= uvicorn main:app

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

すると、以下のように `/openapi.json`, `/docs`, `/redoc` のどの URL にアクセスしても、 `404 Not Found` エラーが返ってくるようになります。

```JSON
{
    "detail": "Not Found"
}
```
