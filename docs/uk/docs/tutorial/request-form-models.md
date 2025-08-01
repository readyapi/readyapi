# Моделі форм (Form Models)

У ReadyAPI Ви можете використовувати **Pydantic-моделі** для оголошення **полів форми**.

/// info | Інформація

Щоб використовувати форми, спочатку встановіть <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">python-multipart</a>.

Переконайтеся, що Ви створили [віртуальне середовище](../virtual-environments.md){.internal-link target=_blank}, активували його, а потім встановили бібліотеку, наприклад:

```console
$ pip install python-multipart
```

///

/// note | Підказка

Ця функція підтримується, починаючи з ReadyAPI версії `0.113.0`. 🤓

///

## Використання Pydantic-моделей для форм

Вам просто потрібно оголосити **Pydantic-модель** з полями, які Ви хочете отримати як **поля форми**, а потім оголосити параметр як `Form`:

{* ../../examples/request_form_models/tutorial001_an_py39.py hl[9:11,15] *}

**ReadyAPI**  **витягне** дані для **кожного поля** з **формових даних** у запиті та надасть вам Pydantic-модель, яку Ви визначили.

## Перевірка документації

Ви можете перевірити це в UI документації за `/docs`:

<div class="screenshot">
<img src="/img/tutorial/request-form-models/image01.png">
</div>

## Заборона додаткових полів форми

У деяких особливих випадках (ймовірно, рідко) Ви можете **обмежити** форму лише тими полями, які були оголошені в Pydantic-моделі, і **заборонити** будь-які **додаткові** поля.

/// note | Підказка

Ця функція підтримується, починаючи з ReadyAPI версії `0.114.0`. 🤓

///

Ви можете використати конфігурацію Pydantic-моделі, щоб заборонити `forbid` будь-які додаткові `extra` поля:

{* ../../examples/request_form_models/tutorial002_an_py39.py hl[12] *}

Якщо клієнт спробує надіслати додаткові дані, він отримає **відповідь з помилкою**.

Наприклад, якщо клієнт спробує надіслати наступні поля форми:

* `username`: `Rick`
* `password`: `Portal Gun`
* `extra`: `Mr. Poopybutthole`

Він отримає відповідь із помилкою, яка повідомляє, що поле `extra` не дозволено:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```

## Підсумок

Ви можете використовувати Pydantic-моделі для оголошення полів форми у ReadyAPI. 😎
