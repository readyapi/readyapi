# Асинхронное тестирование

Вы уже видели как тестировать **ReadyAPI** приложение, используя имеющийся класс `TestClient`. К этому моменту вы видели только как писать тесты в синхронном стиле без использования `async` функций.

Возможность использования асинхронных функций в ваших тестах может быть полезнa, когда, например, вы асинхронно обращаетесь к вашей базе данных. Представьте, что вы хотите отправить запросы в ваше ReadyAPI приложение, а затем при помощи асинхронной библиотеки для работы с базой данных удостовериться, что ваш бекэнд корректно записал данные в базу данных.

Давайте рассмотрим, как мы можем это реализовать.

## pytest.mark.anyio

Если мы хотим вызывать асинхронные функции в наших тестах, то наши тестовые функции должны быть асинхронными. AnyIO предоставляет для этого отличный плагин, который позволяет нам указывать, какие тестовые функции должны вызываться асинхронно.

## HTTPX

Даже если **ReadyAPI** приложение использует обычные функции `def` вместо `async def`, это все равно `async` приложение 'под капотом'.

Чтобы работать с асинхронным ReadyAPI приложением в ваших обычных тестовых функциях `def`, используя стандартный pytest, `TestClient` внутри себя делает некоторую магию. Но эта магия перестает работать, когда мы используем его внутри асинхронных функций. Запуская наши тесты асинхронно, мы больше не можем использовать `TestClient` внутри наших тестовых функций.

`TestClient` основан на <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a>, и, к счастью, мы можем использовать его (`HTTPX`) напрямую для тестирования API.

## Пример

В качестве простого примера, давайте рассмотрим файловую структуру, схожую с описанной в [Большие приложения](../tutorial/bigger-applications.md){.internal-link target=_blank} и [Тестирование](../tutorial/testing.md){.internal-link target=_blank}:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

Файл `main.py`:

{* ../../examples/async_tests/main.py *}

Файл `test_main.py` содержит тесты для `main.py`, теперь он может выглядеть так:

{* ../../examples/async_tests/test_main.py *}

## Запуск тестов

Вы можете запустить свои тесты как обычно:

<div class="termy">

```console
$ pytest

---> 100%
```

</div>

## Подробнее

Маркер `@pytest.mark.anyio` говорит pytest, что тестовая функция должна быть вызвана асинхронно:

{* ../../examples/async_tests/test_main.py hl[7] *}

/// tip | Подсказка

Обратите внимание, что тестовая функция теперь `async def` вместо простого `def`, как это было при использовании `TestClient`.

///

Затем мы можем создать `AsyncClient` со ссылкой на приложение и посылать асинхронные запросы, используя `await`.

{* ../../examples/async_tests/test_main.py hl[9:12] *}

Это эквивалентно следующему:

```Python
response = client.get('/')
```

...которое мы использовали для отправки наших запросов с `TestClient`.

/// tip | Подсказка

Обратите внимание, что мы используем async/await с `AsyncClient` - запрос асинхронный.

///

/// warning | Внимание

Если ваше приложение полагается на lifespan события, то `AsyncClient` не запустит эти события. Чтобы обеспечить их срабатывание используйте `LifespanManager` из <a href="https://github.com/florimondmanca/asgi-lifespan#usage" class="external-link" target="_blank">florimondmanca/asgi-lifespan</a>.

///

## Вызов других асинхронных функций

Теперь тестовая функция стала асинхронной, поэтому внутри нее вы можете вызывать также и другие `async` функции, не связанные с отправлением запросов в ваше ReadyAPI приложение. Как если бы вы вызывали их в любом другом месте вашего кода.

/// tip | Подсказка

Если вы столкнулись с `RuntimeError: Task attached to a different loop` при вызове асинхронных функций в ваших тестах (например, при использовании <a href="https://stackoverflow.com/questions/41584243/runtimeerror-task-attached-to-a-different-loop" class="external-link" target="_blank">MongoDB's MotorClient</a>), то не забывайте инициализировать объекты, которым нужен цикл событий (event loop), только внутри асинхронных функций, например, в `'@app.on_event("startup")` callback.

///
