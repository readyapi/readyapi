# Path Operation の高度な設定

## OpenAPI operationId

/// warning | "注意"

あなたが OpenAPI の「エキスパート」でなければ、これは必要ないかもしれません。

///

_path operation_ で `operation_id` パラメータを利用することで、OpenAPI の `operationId` を設定できます。

`operation_id` は各オペレーションで一意にする必要があります。

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial001.py!}
```

### _path operation 関数_ の名前を operationId として使用する

API の関数名を `operationId` として利用したい場合、すべての API の関数をイテレーションし、各 _path operation_ の `operationId` を `APIRoute.name` で上書きすれば可能です。

そうする場合は、すべての _path operation_ を追加した後に行う必要があります。

```Python hl_lines="2  12-21  24"
{!../../docs_src/path_operation_advanced_configuration/tutorial002.py!}
```

/// tip | "豆知識"

`app.openapi()` を手動でコールする場合、その前に`operationId`を更新する必要があります。

///

/// warning | "注意"

この方法をとる場合、各 _path operation 関数_ が一意な名前である必要があります。

それらが異なるモジュール (Python ファイル) にあるとしてもです。

///

## OpenAPI から除外する

生成される OpenAPI スキーマ (つまり、自動ドキュメント生成の仕組み) から _path operation_ を除外するには、 `include_in_schema` パラメータを `False` にします。

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial003.py!}
```

## docstring による説明の高度な設定

_path operation 関数_ の docstring から OpenAPI に使用する行を制限することができます。

`\f` (「書式送り (Form Feed)」のエスケープ文字) を付与することで、**ReadyAPI** は OpenAPI に使用される出力をその箇所までに制限します。

ドキュメントには表示されませんが、他のツール (例えば Sphinx) では残りの部分を利用できるでしょう。

```Python hl_lines="19-29"
{!../../docs_src/path_operation_advanced_configuration/tutorial004.py!}
```
