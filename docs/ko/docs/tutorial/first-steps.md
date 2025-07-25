# 첫걸음

가장 단순한 ReadyAPI 파일은 다음과 같이 보일 것입니다:

{* ../../examples/first_steps/tutorial001.py *}

위 코드를 `main.py`에 복사합니다.

라이브 서버를 실행합니다:

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

/// note | 참고

`uvicorn main:app` 명령은 다음을 의미합니다:

* `main`: 파일 `main.py` (파이썬 "모듈").
* `app`: `main.py` 내부의 `app = ReadyAPI()` 줄에서 생성한 오브젝트.
* `--reload`: 코드 변경 시 자동으로 서버 재시작. 개발 시에만 사용.

///

출력되는 줄들 중에는 아래와 같은 내용이 있습니다:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

해당 줄은 로컬에서 앱이 서비스되는 URL을 보여줍니다.

### 확인하기

브라우저로 <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a>를 여세요.

아래와 같은 JSON 응답을 볼 수 있습니다:

```JSON
{"message": "Hello World"}
```

### 대화형 API 문서

이제 <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>로 가봅니다.

자동 대화형 API 문서를 볼 수 있습니다 (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> 제공):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### 대안 API 문서

그리고 이제, <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>로 가봅니다.

대안 자동 문서를 볼 수 있습니다 (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> 제공):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

### OpenAPI

**ReadyAPI**는 API를 정의하기 위한 **OpenAPI** 표준을 사용하여 여러분의 모든 API를 이용해 "스키마"를 생성합니다.

#### "스키마"

"스키마"는 무언가의 정의 또는 설명입니다. 이를 구현하는 코드가 아니라 추상적인 설명일 뿐입니다.

#### API "스키마"

<a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a>는 API의 스키마를 어떻게 정의하는지 지시하는 규격입니다.

이 스키마 정의는 API 경로, 가능한 매개변수 등을 포함합니다.

#### 데이터 "스키마"

"스키마"라는 용어는 JSON처럼 어떤 데이터의 형태를 나타낼 수도 있습니다.

이러한 경우 JSON 속성, 가지고 있는 데이터 타입 등을 뜻합니다.

#### OpenAPI와 JSON 스키마

OpenAPI는 당신의 API에 대한 API 스키마를 정의합니다. 또한 이 스키마는 JSON 데이터 스키마의 표준인 **JSON 스키마**를 사용하여 당신의 API가 보내고 받는 데이터의 정의(또는 "스키마")를 포함합니다.

#### `openapi.json` 확인

ReadyAPI는 자동으로 API의 설명과 함께 JSON (스키마)를 생성합니다.

가공되지 않은 OpenAPI 스키마가 어떻게 생겼는지 궁금하다면, 여기에서 직접 볼 수 있습니다: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a>.

다음과 같이 시작하는 JSON을 확인할 수 있습니다:

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

#### OpenAPI의 용도

OpenAPI 스키마는 포함된 두 개의 대화형 문서 시스템을 제공합니다.

그리고 OpenAPI의 모든 것을 기반으로 하는 수십 가지 대안이 있습니다. **ReadyAPI**로 빌드한 애플리케이션에 이러한 대안을 쉽게 추가 할 수 있습니다.

API와 통신하는 클라이언트(프론트엔드, 모바일, IoT 애플리케이션 등)를 위해 코드를 자동으로 생성하는 데도 사용할 수 있습니다.

## 단계별 요약

### 1 단계: `ReadyAPI` 임포트

{* ../../examples/first_steps/tutorial001.py hl[1] *}

`ReadyAPI`는 당신의 API를 위한 모든 기능을 제공하는 파이썬 클래스입니다.

/// note | 기술 세부사항

`ReadyAPI`는 `Starlette`를 직접 상속하는 클래스입니다.

`ReadyAPI`로 <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a>의 모든 기능을 사용할 수 있습니다.

///

### 2 단계: `ReadyAPI` "인스턴스" 생성

{* ../../examples/first_steps/tutorial001.py hl[3] *}

여기에서 `app` 변수는 `ReadyAPI` 클래스의 "인스턴스"가 됩니다.

이것은 당신의 모든 API를 생성하기 위한 상호작용의 주요 지점이 될 것입니다.

이 `app`은 다음 명령에서 `uvicorn`이 참조하고 있는 것과 동일합니다:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

아래처럼 앱을 만든다면:

{* ../../examples/first_steps/tutorial002.py hl[3] *}

이를 `main.py` 파일에 넣고, `uvicorn`을 아래처럼 호출해야 합니다:

<div class="termy">

```console
$ uvicorn main:my_awesome_api --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

### 3 단계: *경로 작동* 생성

#### 경로

여기서 "경로"는 첫 번째 `/`부터 시작하는 URL의 뒷부분을 의미합니다.

그러므로 아래와 같은 URL에서:

```
https://example.com/items/foo
```

...경로는 다음과 같습니다:

```
/items/foo
```

/// info | 정보

"경로"는 일반적으로 "엔드포인트" 또는 "라우트"라고도 불립니다.

///

API를 설계할 때 "경로"는 "관심사"와 "리소스"를 분리하기 위한 주요한 방법입니다.

#### 작동

"작동(Operation)"은 HTTP "메소드" 중 하나를 나타냅니다.

다음 중 하나이며:

* `POST`
* `GET`
* `PUT`
* `DELETE`

...흔히 사용되지 않는 것들도 있습니다:

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

HTTP 프로토콜에서는 이러한 "메소드"를 하나(또는 이상) 사용하여 각 경로와 통신할 수 있습니다.

---

API를 설계할 때 일반적으로 특정 행동을 수행하기 위해 특정 HTTP 메소드를 사용합니다.

일반적으로 다음과 같습니다:

* `POST`: 데이터를 생성하기 위해.
* `GET`: 데이터를 읽기 위해.
* `PUT`: 데이터를 수정하기 위해.
* `DELETE`: 데이터를 삭제하기 위해.

그래서 OpenAPI에서는 각 HTTP 메소드들을 "작동"이라 부릅니다.

우리 역시 이제부터 메소드를 "**작동**"이라고 부를 것입니다.

#### *경로 작동 데코레이터* 정의

{* ../../examples/first_steps/tutorial001.py hl[6] *}

`@app.get("/")`은 **ReadyAPI**에게 바로 아래에 있는 함수가 다음으로 이동하는 요청을 처리한다는 것을 알려줍니다.

* 경로 `/`
* <abbr title="HTTP GET 메소드"><code>get</code> 작동</abbr> 사용

/// info | `@decorator` 정보

이 `@something` 문법은 파이썬에서 "데코레이터"라 부릅니다.

마치 예쁜 장식용(Decorative) 모자처럼(개인적으로 이 용어가 여기서 유래한 것 같습니다) 함수 맨 위에 놓습니다.

"데코레이터"는 아래 있는 함수를 받아 그것으로 무언가를 합니다.

우리의 경우, 이 데코레이터는 **ReadyAPI**에게 아래 함수가 **경로** `/`의 `get` **작동**에 해당한다고 알려줍니다.

이것이 "**경로 작동 데코레이터**"입니다.

///

다른 작동도 사용할 수 있습니다:

* `@app.post()`
* `@app.put()`
* `@app.delete()`

흔히 사용되지 않는 것들도 있습니다:

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

/// tip | 팁

각 작동(HTTP 메소드)을 원하는 대로 사용해도 됩니다.

**ReadyAPI**는 특정 의미를 강제하지 않습니다.

여기서 정보는 지침서일뿐 강제사항이 아닙니다.

예를 들어 GraphQL을 사용하는 경우, 일반적으로 `POST` 작동만 사용하여 모든 행동을 수행합니다.

///

### 4 단계: **경로 작동 함수** 정의

다음은 우리의 "**경로 작동 함수**"입니다:

* **경로**: 는 `/`입니다.
* **작동**: 은 `get`입니다.
* **함수**: 는 "데코레이터" 아래에 있는 함수입니다 (`@app.get("/")` 아래).

{* ../../examples/first_steps/tutorial001.py hl[7] *}

이것은 파이썬 함수입니다.

URL "`/`"에 대한 `GET` 작동을 사용하는 요청을 받을 때마다 **ReadyAPI**에 의해 호출됩니다.

위의 예시에서 이 함수는 `async`(비동기) 함수입니다.

---

`async def`을 이용하는 대신 일반 함수로 정의할 수 있습니다:

{* ../../examples/first_steps/tutorial003.py hl[7] *}

/// note | 참고

차이점을 모르겠다면 [Async: *"바쁘신 경우"*](../async.md#_1){.internal-link target=_blank}을 확인하세요.

///

### 5 단계: 콘텐츠 반환

{* ../../examples/first_steps/tutorial001.py hl[8] *}

`dict`, `list`, 단일값을 가진 `str`, `int` 등을 반환할 수 있습니다.

Pydantic 모델을 반환할 수도 있습니다(나중에 더 자세히 살펴봅니다).

JSON으로 자동 변환되는 객체들과 모델들(ORM 등을 포함해서)이 많이 있습니다. 가장 마음에 드는 것을 사용하십시오, 이미 지원되고 있을 것입니다.

## 요약

* `ReadyAPI` 임포트.
* `app` 인스턴스 생성.
* (`@app.get("/")`처럼) **경로 작동 데코레이터** 작성.
* (위에 있는 `def root(): ...`처럼) **경로 작동 함수** 작성.
* (`uvicorn main:app --reload`처럼) 개발 서버 실행.
