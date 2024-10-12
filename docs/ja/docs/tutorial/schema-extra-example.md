# スキーマの追加 - 例

JSON Schema に追加する情報を定義することができます。

一般的なユースケースはこのドキュメントで示されているように`example`を追加することです。

JSON Schema の追加情報を宣言する方法はいくつかあります。

## Pydantic の`schema_extra`

<a href="https://docs.pydantic.dev/latest/concepts/json_schema/#schema-customization" class="external-link" target="_blank">Pydantic のドキュメント: スキーマのカスタマイズ</a>で説明されているように、`Config`と`schema_extra`を使って Pydantic モデルの例を宣言することができます:

```Python hl_lines="15 16 17 18 19 20 21 22 23"
{!../../docs_src/schema_extra_example/tutorial001.py!}
```

その追加情報はそのまま出力され、JSON Schema に追加されます。

## `Field`の追加引数

後述する`Field`、`Path`、`Query`、`Body`などでは、任意の引数を関数に渡すことで JSON Schema の追加情報を宣言することもできます:

```Python hl_lines="4 10 11 12 13"
{!../../docs_src/schema_extra_example/tutorial002.py!}
```

/// warning | "注意"

これらの追加引数が渡されても、文書化のためのバリデーションは追加されず、注釈だけが追加されることを覚えておいてください。

///

## `Body`の追加引数

追加情報を`Field`に渡すのと同じように、`Path`、`Query`、`Body`などでも同じことができます。

例えば、`Body`にボディリクエストの`example`を渡すことができます:

```Python hl_lines="21 22 23 24 25 26"
{!../../docs_src/schema_extra_example/tutorial003.py!}
```

## ドキュメントの UI の例

上記のいずれの方法でも、`/docs`の中では以下のようになります:

<img src="https://readyapi.khulnasoft.com/img/tutorial/body-fields/image01.png">

## 技術詳細

`example` と `examples`について...

JSON Schema の最新バージョンでは<a href="https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.9.5" class="external-link" target="_blank">`examples`</a>というフィールドを定義していますが、OpenAPI は`examples`を持たない古いバージョンの JSON Schema をベースにしています。

そのため、OpenAPI では同じ目的のために<a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#fixed-fields-20" class="external-link" target="_blank">`example`</a>を独自に定義しており（`examples`ではなく`example`として）、それが docs UI（Swagger UI を使用）で使用されています。

つまり、`example`は JSON Schema の一部ではありませんが、OpenAPI の一部であり、それが docs UI で使用されることになります。

## その他の情報

同じように、フロントエンドのユーザーインターフェースなどをカスタマイズするために、各モデルの JSON Schema に追加される独自の追加情報を追加することができます。
