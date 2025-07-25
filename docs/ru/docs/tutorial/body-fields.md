# Body - Поля

Таким же способом, как вы объявляете дополнительную валидацию и метаданные в параметрах *функции обработки пути* с помощью функций `Query`, `Path` и `Body`, вы можете объявлять валидацию и метаданные внутри Pydantic моделей, используя функцию `Field` из Pydantic.

## Импорт `Field`

Сначала вы должны импортировать его:

{* ../../examples/body_fields/tutorial001_py310.py hl[2] *}

/// warning | Внимание

Обратите внимание, что функция `Field` импортируется непосредственно из `pydantic`, а не из `readyapi`, как все остальные функции (`Query`, `Path`, `Body` и т.д.).

///

## Объявление атрибутов модели

Вы можете использовать функцию `Field` с атрибутами модели:

{* ../../examples/body_fields/tutorial001_py310.py hl[9:12] *}

Функция `Field` работает так же, как `Query`, `Path` и `Body`, у неё такие же параметры и т.д.

/// note | Технические детали

На самом деле, `Query`, `Path` и другие функции, которые вы увидите в дальнейшем, создают объекты подклассов общего класса `Param`, который сам по себе является подклассом `FieldInfo` из Pydantic.

И `Field` (из Pydantic), и `Body`, оба возвращают объекты подкласса `FieldInfo`.

У класса `Body` есть и другие подклассы, с которыми вы ознакомитесь позже.

Помните, что когда вы импортируете `Query`, `Path` и другое из `readyapi`, это фактически функции, которые возвращают специальные классы.

///

/// tip | Подсказка

Обратите внимание, что каждый атрибут модели с типом, значением по умолчанию и `Field` имеет ту же структуру, что и параметр *функции обработки пути* с `Field` вместо `Path`, `Query` и `Body`.

///

## Добавление дополнительной информации

Вы можете объявлять дополнительную информацию в `Field`, `Query`, `Body` и т.п. Она будет включена в сгенерированную JSON схему.

Вы узнаете больше о добавлении дополнительной информации позже в документации, когда будете изучать, как задавать примеры принимаемых данных.


/// warning | Внимание

Дополнительные ключи, переданные в функцию `Field`, также будут присутствовать в сгенерированной OpenAPI схеме вашего приложения.
Поскольку эти ключи не являются обязательной частью спецификации OpenAPI, некоторые инструменты OpenAPI, например, [валидатор OpenAPI](https://validator.swagger.io/), могут не работать с вашей сгенерированной схемой.

///

## Резюме

Вы можете использовать функцию `Field` из Pydantic, чтобы задавать дополнительную валидацию и метаданные для атрибутов модели.

Вы также можете использовать дополнительные ключевые аргументы, чтобы добавить метаданные JSON схемы.
