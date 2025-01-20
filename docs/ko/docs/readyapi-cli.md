# ReadyAPI CLI

**ReadyAPI CLI**는 ReadyAPI 애플리케이션을 실행하고, 프로젝트를 관리하는 등 다양한 작업을 수행할 수 있는 커맨드 라인 프로그램입니다.

ReadyAPI를 설치할 때 (예: `pip install "readyapi[standard]"` 명령어를 사용할 경우), `readyapi-cli`라는 패키지가 포함됩니다. 이 패키지는 터미널에서 사용할 수 있는 `readyapi` 명령어를 제공합니다.

개발용으로 ReadyAPI 애플리케이션을 실행하려면 다음과 같이 `readyapi dev` 명령어를 사용할 수 있습니다:

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

`readyapi`라고 불리는 명령어 프로그램은 **ReadyAPI CLI**입니다.

ReadyAPI CLI는 Python 프로그램의 경로(예: `main.py`)를 인수로 받아, `ReadyAPI` 인스턴스(일반적으로 `app`으로 명명)를 자동으로 감지하고 올바른 임포트 과정을 결정한 후 이를 실행합니다.

프로덕션 환경에서는 `readyapi run` 명령어를 사용합니다. 🚀

내부적으로, **ReadyAPI CLI**는 고성능의, 프로덕션에 적합한, ASGI 서버인 <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>을 사용합니다. 😎

## `readyapi dev`

`readyapi dev` 명령을 실행하면 개발 모드가 시작됩니다.

기본적으로 **자동 재시작(auto-reload)** 기능이 활성화되어, 코드에 변경이 생기면 서버를 자동으로 다시 시작합니다. 하지만 이 기능은 리소스를 많이 사용하며, 비활성화했을 때보다 안정성이 떨어질 수 있습니다. 따라서 개발 환경에서만 사용하는 것이 좋습니다. 또한, 서버는 컴퓨터가 자체적으로 통신할 수 있는 IP 주소(`localhost`)인 `127.0.0.1`에서 연결을 대기합니다.

## `readyapi run`

`readyapi run` 명령을 실행하면 기본적으로 프로덕션 모드로 ReadyAPI가 시작됩니다.

기본적으로 **자동 재시작(auto-reload)** 기능이 비활성화되어 있습니다. 또한, 사용 가능한 모든 IP 주소인 `0.0.0.0`에서 연결을 대기하므로 해당 컴퓨터와 통신할 수 있는 모든 사람이 공개적으로 액세스할 수 있습니다. 이는 일반적으로 컨테이너와 같은 프로덕션 환경에서 실행하는 방법입니다.

애플리케이션을 배포하는 방식에 따라 다르지만, 대부분 "종료 프록시(termination proxy)"를 활용해 HTTPS를 처리하는 것이 좋습니다. 배포 서비스 제공자가 이 작업을 대신 처리해줄 수도 있고, 직접 설정해야 할 수도 있습니다.

/// tip

자세한 내용은 [deployment documentation](deployment/index.md){.internal-link target=\_blank}에서 확인할 수 있습니다.

///
