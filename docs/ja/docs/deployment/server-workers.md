# Server Workers - Gunicorn と Uvicorn

前回のデプロイメントのコンセプトを振り返ってみましょう：

- セキュリティ - HTTPS
- 起動時の実行
- 再起動
- **レプリケーション（実行中のプロセス数）**
- メモリ
- 開始前の事前ステップ

ここまでのドキュメントのチュートリアルでは、おそらく Uvicorn のような**サーバープログラム**を**単一のプロセス**で実行しています。

アプリケーションをデプロイする際には、**複数のコア**を利用し、そしてより多くのリクエストを処理できるようにするために、プロセスの**レプリケーション**を持つことを望むでしょう。

前のチャプターである[デプロイメントのコンセプト](concepts.md){.internal-link target=\_blank}にて見てきたように、有効な戦略がいくつかあります。

ここでは<a href="https://gunicorn.org/" class="external-link" target="_blank">**Gunicorn**</a>が**Uvicorn のワーカー・プロセス**を管理する場合の使い方について紹介していきます。

/// info

<!-- NOTE: the current version of docker.md is outdated compared to English one.  -->

Docker や Kubernetes などのコンテナを使用している場合は、次の章で詳しく説明します： [コンテナ内の ReadyAPI - Docker](docker.md){.internal-link target=\_blank}

特に**Kubernetes**上で実行する場合は、おそらく**Gunicorn を使用せず**、**コンテナごとに単一の Uvicorn プロセス**を実行することになりますが、それについてはこの章の後半で説明します。

///

## Gunicorn による Uvicorn のワーカー・プロセスの管理

**Gunicorn**は**WSGI 標準**のアプリケーションサーバーです。このことは、Gunicorn は Flask や Django のようなアプリケーションにサービスを提供できることを意味します。Gunicorn それ自体は**ReadyAPI**と互換性がないですが、というのも ReadyAPI は最新の**<a href="https://asgi.readthedocs.io/en/latest/" class="external-link" target="_blank">ASGI 標準</a>**を使用しているためです。

しかし、Gunicorn は**プロセスマネージャー**として動作し、ユーザーが特定の**ワーカー・プロセスクラス**を使用するように指示することができます。すると Gunicorn はそのクラスを使い 1 つ以上の**ワーカー・プロセス**を開始します。

そして**Uvicorn**には**Gunicorn 互換のワーカークラス**があります。

この組み合わせで、Gunicorn は**プロセスマネージャー**として動作し、**ポート**と**IP**をリッスンします。そして、**Uvicorn クラス**を実行しているワーカー・プロセスに通信を**転送**します。

そして、Gunicorn 互換の**Uvicorn ワーカー**クラスが、ReadyAPI が使えるように、Gunicorn から送られてきたデータを ASGI 標準に変換する役割を担います。

## Gunicorn と Uvicorn をインストールする

<div class="termy">

```console
$ pip install "uvicorn[standard]" gunicorn

---> 100%
```

</div>

これにより Uvicorn と（高性能を得るための）標準（`standard`）の追加パッケージと Gunicorn の両方がインストールされます。

## Uvicorn のワーカーとともに Gunicorn を実行する

Gunicorn を以下のように起動させることができます:

<div class="termy">

```console
$ gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80

[19499] [INFO] Starting gunicorn 20.1.0
[19499] [INFO] Listening at: http://0.0.0.0:80 (19499)
[19499] [INFO] Using worker: uvicorn.workers.UvicornWorker
[19511] [INFO] Booting worker with pid: 19511
[19513] [INFO] Booting worker with pid: 19513
[19514] [INFO] Booting worker with pid: 19514
[19515] [INFO] Booting worker with pid: 19515
[19511] [INFO] Started server process [19511]
[19511] [INFO] Waiting for application startup.
[19511] [INFO] Application startup complete.
[19513] [INFO] Started server process [19513]
[19513] [INFO] Waiting for application startup.
[19513] [INFO] Application startup complete.
[19514] [INFO] Started server process [19514]
[19514] [INFO] Waiting for application startup.
[19514] [INFO] Application startup complete.
[19515] [INFO] Started server process [19515]
[19515] [INFO] Waiting for application startup.
[19515] [INFO] Application startup complete.
```

</div>

それぞれのオプションの意味を見てみましょう：

- `main:app`： `main`は"`main`"という名前の Python モジュール、つまりファイル`main.py`を意味します。そして `app` は **ReadyAPI** アプリケーションの変数名です。

  - main:app`はPythonの`import`文と同じようなものだと想像できます：

    ```Python
    from main import app
    ```

  - つまり、`main:app`のコロンは、`from main import app`の Python の`import`の部分と同じになります。

- `--workers`： 使用するワーカー・プロセスの数で、それぞれが Uvicorn のワーカーを実行します。

- `--worker-class`： ワーカー・プロセスで使用する Gunicorn 互換のワーカークラスです。

  - ここでは Gunicorn がインポートして使用できるクラスを渡します：

    ```Python
    import uvicorn.workers.UvicornWorker
    ```

- `--bind`： Gunicorn にリッスンする IP とポートを伝えます。コロン(`:`)で IP とポートを区切ります。
  - Uvicorn を直接実行している場合は、`--bind 0.0.0.0:80` （Gunicorn のオプション）の代わりに、`--host 0.0.0.0`と `--port 80`を使います。

出力では、各プロセスの**PID**（プロセス ID）が表示されているのがわかります（単なる数字です）。

以下の通りです：

- Gunicorn の**プロセス・マネージャー**は PID `19499`（あなたの場合は違う番号でしょう）で始まります。
- 次に、`Listening at: http://0.0.0.0:80`を開始します。
- それから `uvicorn.workers.UvicornWorker` でワーカークラスを使用することを検出します。
- そして、**4 つのワーカー**を起動します。それぞれのワーカーの PID は、`19511`、`19513`、`19514`、`19515`です。

Gunicorn はまた、ワーカーの数を維持するために必要であれば、**ダウンしたプロセス**を管理し、**新しいプロセスを**再起動**させます。そのため、上記のリストにある**再起動\*\*の概念に一部役立ちます。

しかしながら、必要であれば Gunicorn を**再起動**させ、**起動時に実行**させるなど、外部のコンポーネントを持たせることも必要かもしれません。

## Uvicorn とワーカー

Uvicorn には複数の**ワーカー・プロセス**を起動し実行するオプションもあります。

とはいうものの、今のところ Uvicorn のワーカー・プロセスを扱う機能は Gunicorn よりも制限されています。そのため、このレベル（Python レベル）でプロセスマネージャーを持ちたいのであれば、Gunicorn をプロセスマネージャーとして使ってみた方が賢明かもしれないです。

どんな場合であれ、以下のように実行します：

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
<font color="#A6E22E">INFO</font>:     Uvicorn running on <b>http://0.0.0.0:8080</b> (Press CTRL+C to quit)
<font color="#A6E22E">INFO</font>:     Started parent process [<font color="#A1EFE4"><b>27365</b></font>]
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27368</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27369</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27370</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27367</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
```

</div>

ここで唯一の新しいオプションは `--workers` で、Uvicorn に 4 つのワーカー・プロセスを起動するように指示しています。

各プロセスの **PID** が表示され、親プロセスの `27365` (これは **プロセスマネージャ**) と、各ワーカー・プロセスの **PID** が表示されます： `27368`、`27369`、`27370`、`27367`になります。

## デプロイメントのコンセプト

ここでは、アプリケーションの実行を**並列化**し、CPU の**マルチコア**を活用し、**より多くのリクエスト**に対応できるようにするために、**Gunicorn**（または Uvicorn）を使用して**Uvicorn ワーカー・プロセス**を管理する方法を見ていきました。

上記のデプロイのコンセプトのリストから、ワーカーを使うことは主に**レプリケーション**の部分と、**再起動**を少し助けてくれます：

- セキュリティ - HTTPS
- 起動時の実行
- 再起動
- レプリケーション（実行中のプロセス数）
- メモリー
- 開始前の事前のステップ

## コンテナと Docker

<!-- NOTE: the current version of docker.md is outdated compared to English one.  -->

次章の[コンテナ内の ReadyAPI - Docker](docker.md){.internal-link target=\_blank}では、その他の**デプロイのコンセプト**を扱うために実施するであろう戦略をいくつか紹介します。

また、**Gunicorn と Uvicorn ワーカー**を含む**公式 Docker イメージ**と、簡単なケースに役立ついくつかのデフォルト設定も紹介します。

また、(Gunicorn を使わずに)Uvicorn プロセスを 1 つだけ実行するために、**ゼロから独自のイメージを**構築する方法も紹介します。これは簡単なプロセスで、おそらく**Kubernetes**のような分散コンテナ管理システムを使うときにやりたいことでしょう。

## まとめ

Uvicorn ワーカーを使ったプロセスマネージャとして**Gunicorn**（または Uvicorn）を使えば、**マルチコア CPU**を活用して**複数のプロセスを並列実行**できます。

これらのツールやアイデアは、**あなた自身のデプロイシステム**をセットアップしながら、他のデプロイコンセプトを自分で行う場合にも使えます。

次の章では、コンテナ（Docker や Kubernetes など）を使った**ReadyAPI**について学んでいきましょう。これらのツールには、他の**デプロイのコンセプト**も解決する簡単な方法があることがわかるでしょう。✨
