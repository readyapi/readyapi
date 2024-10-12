# レスポンスモデル

_path operations_ のいずれにおいても、`response_model`パラメータを使用して、レスポンスのモデルを宣言することができます:

- `@app.get()`
- `@app.post()`
- `@app.put()`
- `@app.delete()`
- など。

```Python hl_lines="17"
{!../../docs_src/response_model/tutorial001.py!}
```

/// note | "備考"

`response_model`は「デコレータ」メソッド（`get`、`post`など）のパラメータであることに注意してください。すべてのパラメータやボディのように、_path operation 関数_ のパラメータではありません。

///

Pydantic モデルの属性に対して宣言するのと同じ型を受け取るので、Pydantic モデルになることもできますが、例えば、`List[Item]`のような Pydantic モデルの`list`になることもできます。

ReadyAPI は`response_model`を使って以下のことをします:

- 出力データを型宣言に変換します。
- データを検証します。
- OpenAPI の _path operation_ で、レスポンス用の JSON Schema を追加します。
- 自動ドキュメントシステムで使用されます。

しかし、最も重要なのは:

- 出力データをモデルのデータに限定します。これがどのように重要なのか以下で見ていきましょう。

/// note | "技術詳細"

レスポンスモデルは、関数の戻り値のアノテーションではなく、このパラメータで宣言されています。なぜなら、パス関数は実際にはそのレスポンスモデルを返すのではなく、`dict`やデータベースオブジェクト、あるいは他のモデルを返し、`response_model`を使用してフィールドの制限やシリアライズを行うからです。

///

## 同じ入力データの返却

ここでは`UserIn`モデルを宣言しています。それには平文のパスワードが含まれています:

```Python hl_lines="9 11"
{!../../docs_src/response_model/tutorial002.py!}
```

そして、このモデルを使用して入力を宣言し、同じモデルを使って出力を宣言しています:

```Python hl_lines="17 18"
{!../../docs_src/response_model/tutorial002.py!}
```

これで、ブラウザがパスワードを使ってユーザーを作成する際に、API がレスポンスで同じパスワードを返すようになりました。

この場合、ユーザー自身がパスワードを送信しているので問題ないかもしれません。

しかし、同じモデルを別の*path operation*に使用すると、すべてのクライアントにユーザーのパスワードを送信してしまうことになります。

/// danger | "危険"

ユーザーの平文のパスワードを保存したり、レスポンスで送信したりすることは絶対にしないでください。

///

## 出力モデルの追加

代わりに、平文のパスワードを持つ入力モデルと、パスワードを持たない出力モデルを作成することができます:

```Python hl_lines="9 11 16"
{!../../docs_src/response_model/tutorial003.py!}
```

ここでは、*path operation 関数*がパスワードを含む同じ入力ユーザーを返しているにもかかわらず:

```Python hl_lines="24"
{!../../docs_src/response_model/tutorial003.py!}
```

...`response_model`を`UserOut`と宣言したことで、パスワードが含まれていません:

```Python hl_lines="22"
{!../../docs_src/response_model/tutorial003.py!}
```

そのため、**ReadyAPI** は出力モデルで宣言されていない全てのデータをフィルタリングしてくれます（Pydantic を使用）。

## ドキュメントを見る

自動ドキュメントを見ると、入力モデルと出力モデルがそれぞれ独自の JSON Schema を持っていることが確認できます。

<img src="https://readyapi.khulnasoft.com/img/tutorial/response-model/image01.png">

そして、両方のモデルは、対話型の API ドキュメントに使用されます:

<img src="https://readyapi.khulnasoft.com/img/tutorial/response-model/image02.png">

## レスポンスモデルのエンコーディングパラメータ

レスポンスモデルにはデフォルト値を設定することができます:

```Python hl_lines="11 13 14"
{!../../docs_src/response_model/tutorial004.py!}
```

- `description: str = None`は`None`がデフォルト値です。
- `tax: float = 10.5`は`10.5`がデフォルト値です。
- `tags: List[str] = []` は空のリスト（`[]`）がデフォルト値です。

しかし、実際に保存されていない場合には結果からそれらを省略した方が良いかもしれません。

例えば、NoSQL データベースに多くのオプション属性を持つモデルがあるが、デフォルト値でいっぱいの非常に長い JSON レスポンスを送信したくない場合です。

### `response_model_exclude_unset`パラメータの使用

*path operation デコレータ*に`response_model_exclude_unset=True`パラメータを設定することができます:

```Python hl_lines="24"
{!../../docs_src/response_model/tutorial004.py!}
```

そして、これらのデフォルト値はレスポンスに含まれず、実際に設定された値のみが含まれます。

そのため、*path operation*に ID`foo`が設定された item のリクエストを送ると、レスポンスは以下のようになります（デフォルト値を含まない）:

```JSON
{
    "name": "Foo",
    "price": 50.2
}
```

/// info | "情報"

ReadyAPI はこれをするために、Pydantic モデルの`.dict()`を<a href="https://docs.pydantic.dev/latest/concepts/serialization/#modeldict" class="external-link" target="_blank">その`exclude_unset`パラメータ</a>で使用しています。

///

/// info | "情報"

以下も使用することができます:

- `response_model_exclude_defaults=True`
- `response_model_exclude_none=True`

`exclude_defaults`と`exclude_none`については、<a href="https://docs.pydantic.dev/latest/concepts/serialization/#modeldict" class="external-link" target="_blank">Pydantic のドキュメント</a>で説明されている通りです。

///

#### デフォルト値を持つフィールドの値を持つデータ

しかし、ID`bar`の item のように、デフォルト値が設定されているモデルのフィールドに値が設定されている場合:

```Python hl_lines="3 5"
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
```

それらはレスポンスに含まれます。

#### デフォルト値と同じ値を持つデータ

ID`baz`の item のようにデフォルト値と同じ値を持つデータの場合:

```Python hl_lines="3 5 6"
{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

ReadyAPI は十分に賢いので（実際には、Pydantic が十分に賢い）`description`や`tax`、`tags`はデフォルト値と同じ値を持っているにもかかわらず、明示的に設定されていることを理解しています。（デフォルトから取得するのではなく）

そのため、それらは JSON レスポンスに含まれることになります。

/// tip | "豆知識"

デフォルト値は`None`だけでなく、なんでも良いことに注意してください。
例えば、リスト（`[]`）や`10.5`の`float`などです。

///

### `response_model_include`と`response_model_exclude`

*path operation デコレータ*として`response_model_include`と`response_model_exclude`も使用することができます。

属性名を持つ`str`の`set`を受け取り、含める(残りを省略する)か、除外(残りを含む)します。

これは、Pydantic モデルが１つしかなく、出力からいくつかのデータを削除したい場合のクイックショートカットとして使用することができます。

/// tip | "豆知識"

それでも、これらのパラメータではなく、複数のクラスを使用して、上記のようなアイデアを使うことをおすすめします。

これは`response_model_include`や`response_mode_exclude`を使用していくつかの属性を省略しても、アプリケーションの OpenAPI（とドキュメント）で生成された JSON Schema が完全なモデルになるからです。

同様に動作する`response_model_by_alias`にも当てはまります。

///

```Python hl_lines="31 37"
{!../../docs_src/response_model/tutorial005.py!}
```

/// tip | "豆知識"

`{"name", "description"}`の構文はこれら２つの値をもつ`set`を作成します。

これは`set(["name", "description"])`と同等です。

///

#### `set`の代わりに`list`を使用する

もし`set`を使用することを忘れて、代わりに`list`や`tuple`を使用しても、ReadyAPI はそれを`set`に変換して正しく動作します:

```Python hl_lines="31 37"
{!../../docs_src/response_model/tutorial006.py!}
```

## まとめ

_path operation デコレータの_`response_model`パラメータを使用して、レスポンスモデルを定義し、特にプライベートデータがフィルタリングされていることを保証します。

明示的に設定された値のみを返すには、`response_model_exclude_unset`を使用します。
