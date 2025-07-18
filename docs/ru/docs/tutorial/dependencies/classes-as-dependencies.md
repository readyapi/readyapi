# Классы как зависимости

Прежде чем углубиться в систему **Внедрения Зависимостей**, давайте обновим предыдущий пример.

## `Словарь` из предыдущего примера

В предыдущем примере мы возвращали `словарь` из нашей зависимости:

{* ../../examples/dependencies/tutorial001_an_py310.py hl[9] *}

Но затем мы получаем `словарь`  в параметре `commons`  *функции операции пути*. И мы знаем, что редакторы не могут обеспечить достаточную поддержку для `словаря`, поскольку они не могут знать их ключи и типы значений.

Мы можем сделать лучше...

## Что делает зависимость

До сих пор вы видели зависимости, объявленные как функции.

Но это не единственный способ объявления зависимостей (хотя, вероятно, более распространенный).

Ключевым фактором является то, что зависимость должна быть "вызываемой".

В Python "**вызываемый**" - это все, что Python может "вызвать", как функцию.

Так, если у вас есть объект `something` (который может _не_ быть функцией) и вы можете "вызвать" его (выполнить) как:

```Python
something()
```

или

```Python
something(some_argument, some_keyword_argument="foo")
```

в таком случае он является "вызываемым".

## Классы как зависимости

Вы можете заметить, что для создания экземпляра класса в Python используется тот же синтаксис.

Например:

```Python
class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")
```

В данном случае `fluffy` является экземпляром класса `Cat`.

А чтобы создать `fluffy`, вы "вызываете" `Cat`.

Таким образом, класс в Python также является **вызываемым**.

Тогда в **ReadyAPI** в качестве зависимости можно использовать класс Python.

На самом деле ReadyAPI проверяет, что переданный объект является "вызываемым" (функция, класс или что-либо еще) и указаны  необходимые для его вызова параметры.

Если вы передаёте что-то, что можно "вызывать" в качестве зависимости в **ReadyAPI**, то он будет анализировать параметры, необходимые для "вызова" этого объекта и обрабатывать их так же, как параметры *функции операции пути*. Включая подзависимости.

Это относится и к вызываемым объектам без параметров. Работа с ними происходит точно так же, как и для *функций операции пути* без параметров.

Теперь мы можем изменить зависимость `common_parameters`, указанную выше, на класс `CommonQueryParams`:

{* ../../examples/dependencies/tutorial002_an_py310.py hl[11:15] *}

Обратите внимание на метод `__init__`, используемый для создания экземпляра класса:

{* ../../examples/dependencies/tutorial002_an_py310.py hl[12] *}

...имеет те же параметры, что и ранее используемая функция `common_parameters`:

{* ../../examples/dependencies/tutorial001_an_py310.py hl[8] *}

Эти параметры и будут использоваться **ReadyAPI** для "решения" зависимости.

В обоих случаях она будет иметь:

* Необязательный параметр запроса `q`, представляющий собой `str`.
* Параметр запроса `skip`, представляющий собой `int`, по умолчанию `0`.
* Параметр запроса `limit`, представляющий собой `int`, по умолчанию равный `100`.

В обоих случаях данные будут конвертированы, валидированы, документированы по схеме OpenAPI и т.д.

## Как это использовать

Теперь вы можете объявить свою зависимость, используя этот класс.

{* ../../examples/dependencies/tutorial002_an_py310.py hl[19] *}

**ReadyAPI** вызывает класс `CommonQueryParams`. При этом создается "экземпляр" этого класса, который будет передан в качестве параметра `commons` в вашу функцию.

## Аннотация типа или `Depends`

Обратите внимание, что в приведенном выше коде мы два раза пишем `CommonQueryParams`:

//// tab | Python 3.6+ без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

//// tab | Python 3.6+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

Последний параметр `CommonQueryParams`, в:

```Python
... Depends(CommonQueryParams)
```

...это то, что **ReadyAPI** будет использовать, чтобы узнать, что является зависимостью.

Из него ReadyAPI извлечёт объявленные параметры и именно их будет вызывать.

---

В этом случае первый `CommonQueryParams`, в:

//// tab | Python 3.6+

```Python
commons: Annotated[CommonQueryParams, ...
```

////

//// tab | Python 3.6+ без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons: CommonQueryParams ...
```

////

...не имеет никакого специального значения для **ReadyAPI**. ReadyAPI не будет использовать его для преобразования данных, валидации и т.д. (поскольку для этого используется `Depends(CommonQueryParams)`).

На самом деле можно написать просто:

//// tab | Python 3.6+

```Python
commons: Annotated[Any, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.6+ без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons = Depends(CommonQueryParams)
```

////

...как тут:

{* ../../examples/dependencies/tutorial003_an_py310.py hl[19] *}

Но объявление типа приветствуется, так как в этом случае ваш редактор будет знать, что будет передано в качестве параметра `commons`, и тогда он сможет помочь вам с автодополнением, проверкой типов и т.д:

<img src="/img/tutorial/dependencies/image02.png">

## Сокращение

Но вы видите, что здесь мы имеем некоторое повторение кода, дважды написав `CommonQueryParams`:

//// tab | Python 3.6+ без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

//// tab | Python 3.6+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

Для случаев, когда зависимостью является *конкретный* класс, который **ReadyAPI** "вызовет" для создания экземпляра этого класса, можно использовать укороченную запись.


Вместо того чтобы писать:

//// tab | Python 3.6+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.6+ без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

...следует написать:

//// tab | Python 3.6+

```Python
commons: Annotated[CommonQueryParams, Depends()]
```

////

//// tab | Python 3.6 без Annotated

/// tip | Подсказка

Рекомендуется использовать версию с `Annotated` если возможно.

///

```Python
commons: CommonQueryParams = Depends()
```

////

Вы объявляете зависимость как тип параметра и используете `Depends()` без какого-либо параметра, вместо того чтобы *снова* писать полный класс внутри `Depends(CommonQueryParams)`.

Аналогичный пример будет выглядеть следующим образом:

{* ../../examples/dependencies/tutorial004_an_py310.py hl[19] *}

...и **ReadyAPI** будет знать, что делать.

/// tip | Подсказка

Если это покажется вам более запутанным, чем полезным, не обращайте внимания, это вам не *нужно*.

Это просто сокращение. Потому что **ReadyAPI** заботится о том, чтобы помочь вам свести к минимуму повторение кода.

///
