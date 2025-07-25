# JSON кодировщик

В некоторых случаях может потребоваться преобразование типа данных (например, Pydantic-модели) в тип, совместимый с JSON (например, `dict`, `list` и т.д.).

Например, если необходимо хранить его в базе данных.

Для этого **ReadyAPI** предоставляет функцию `jsonable_encoder()`.

## Использование `jsonable_encoder`

Представим, что у вас есть база данных `fake_db`, которая принимает только JSON-совместимые данные.

Например, он не принимает объекты `datetime`, так как они не совместимы с JSON.

В таком случае объект `datetime` следует преобразовать в строку соответствующую <a href="https://en.wikipedia.org/wiki/ISO_8601" class="external-link" target="_blank">формату ISO</a>.

Точно так же эта база данных не может принять Pydantic модель (объект с атрибутами), а только `dict`.

Для этого можно использовать функцию `jsonable_encoder`.

Она принимает объект, например, модель Pydantic, и возвращает его версию, совместимую с JSON:

{* ../../examples/encoder/tutorial001_py310.py hl[4,21] *}

В данном примере она преобразует Pydantic модель в `dict`, а `datetime` - в `str`.

Результатом её вызова является объект, который может быть закодирован с помощью функции из стандартной библиотеки Python – <a href="https://docs.python.org/3/library/json.html#json.dumps" class="external-link" target="_blank">`json.dumps()`</a>.

Функция не возвращает большой `str`, содержащий данные в формате JSON (в виде строки). Она возвращает стандартную структуру данных Python (например, `dict`) со значениями и подзначениями, которые совместимы с JSON.

/// note | Технические детали

`jsonable_encoder` фактически используется **ReadyAPI** внутри системы для преобразования данных. Однако он полезен и во многих других сценариях.

///
