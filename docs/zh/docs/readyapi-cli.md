# ReadyAPI CLI

**ReadyAPI CLI** 是一个命令行程序，你可以用它来部署和运行你的 ReadyAPI 应用程序，管理你的 ReadyAPI 项目，等等。

当你安装 ReadyAPI 时（例如使用 `pip install ReadyAPI` 命令），会包含一个名为 `readyapi-cli` 的软件包，该软件包在终端中提供 `readyapi` 命令。

要在开发环境中运行你的 ReadyAPI 应用，你可以使用 `readyapi dev` 命令：

<div class="termy">

```console
$ <font color="#4E9A06">readyapi</font> dev <u style="text-decoration-style:single">main.py</u>
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

 <span style="background-color:#C4A000"><font color="#2E3436">╭────────── ReadyAPI CLI - Development mode ───────────╮</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│                                                     │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│  Serving at: http://127.0.0.1:8000                  │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│                                                     │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│  API docs: http://127.0.0.1:8000/docs               │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│                                                     │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│  Running in development mode, for production use:   │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│                                                     │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│  </font></span><span style="background-color:#C4A000"><font color="#555753"><b>readyapi run</b></font></span><span style="background-color:#C4A000"><font color="#2E3436">                                        │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">│                                                     │</font></span>
 <span style="background-color:#C4A000"><font color="#2E3436">╰─────────────────────────────────────────────────────╯</font></span>

<font color="#4E9A06">INFO</font>:     Will watch for changes in these directories: [&apos;/home/user/code/awesomeapp&apos;]
<font color="#4E9A06">INFO</font>:     Uvicorn running on <b>http://127.0.0.1:8000</b> (Press CTRL+C to quit)
<font color="#4E9A06">INFO</font>:     Started reloader process [<font color="#34E2E2"><b>2265862</b></font>] using <font color="#34E2E2"><b>WatchFiles</b></font>
<font color="#4E9A06">INFO</font>:     Started server process [<font color="#06989A">2265873</font>]
<font color="#4E9A06">INFO</font>:     Waiting for application startup.
<font color="#4E9A06">INFO</font>:     Application startup complete.
```

</div>

该命令行程序 `readyapi` 就是 **ReadyAPI CLI**。

ReadyAPI CLI 接收你的 Python 程序路径，自动检测包含 ReadyAPI 的变量（通常命名为 `app`）及其导入方式，然后启动服务。

在生产环境中，你应该使用 `readyapi run` 命令。🚀

在内部，**ReadyAPI CLI** 使用了 <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>，这是一个高性能、适用于生产环境的 ASGI 服务器。😎

## `readyapi dev`

当你运行 `readyapi dev` 时，它将以开发模式运行。

默认情况下，它会启用**自动重载**，因此当你更改代码时，它会自动重新加载服务器。该功能是资源密集型的，且相较不启用时更不稳定，因此你应该仅在开发环境下使用它。

默认情况下，它将监听 IP 地址 `127.0.0.1`，这是你的机器与自身通信的 IP 地址（`localhost`）。

## `readyapi run`

当你运行 `readyapi run` 时，它默认以生产环境模式运行。

默认情况下，**自动重载是禁用的**。

它将监听 IP 地址 `0.0.0.0`，即所有可用的 IP 地址，这样任何能够与该机器通信的人都可以公开访问它。这通常是你在生产环境中运行它的方式，例如在容器中运行。

在大多数情况下，你会（且应该）有一个“终止代理”在上层为你处理 HTTPS，这取决于你如何部署应用程序，你的服务提供商可能会为你处理此事，或者你可能需要自己设置。

/// tip | 提示

你可以在 [deployment documentation](deployment/index.md){.internal-link target=_blank} 获得更多信息。

///
