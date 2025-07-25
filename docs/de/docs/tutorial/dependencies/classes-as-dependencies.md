# Klassen als Abhängigkeiten

Bevor wir tiefer in das **Dependency Injection** System eintauchen, lassen Sie uns das vorherige Beispiel verbessern.

## Ein `dict` aus dem vorherigen Beispiel

Im vorherigen Beispiel haben wir ein `dict` von unserer Abhängigkeit („Dependable“) zurückgegeben:

{* ../../examples/dependencies/tutorial001_an_py310.py hl[9] *}

Aber dann haben wir ein `dict` im Parameter `commons` der *Pfadoperation-Funktion*.

Und wir wissen, dass Editoren nicht viel Unterstützung (wie etwa Code-Vervollständigung) für `dict`s bieten können, weil sie ihre Schlüssel- und Werttypen nicht kennen.

Das können wir besser machen ...

## Was macht eine Abhängigkeit aus

Bisher haben Sie Abhängigkeiten gesehen, die als Funktionen deklariert wurden.

Das ist jedoch nicht die einzige Möglichkeit, Abhängigkeiten zu deklarieren (obwohl es wahrscheinlich die gebräuchlichste ist).

Der springende Punkt ist, dass eine Abhängigkeit aufrufbar („callable“) sein sollte.

Ein „**Callable**“ in Python ist etwas, das wie eine Funktion aufgerufen werden kann („to call“).

Wenn Sie also ein Objekt `something` haben (das möglicherweise _keine_ Funktion ist) und Sie es wie folgt aufrufen (ausführen) können:

```Python
something()
```

oder

```Python
something(some_argument, some_keyword_argument="foo")
```

dann ist das ein „Callable“ (ein „Aufrufbares“).

## Klassen als Abhängigkeiten

Möglicherweise stellen Sie fest, dass Sie zum Erstellen einer Instanz einer Python-Klasse die gleiche Syntax verwenden.

Zum Beispiel:

```Python
class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")
```

In diesem Fall ist `fluffy` eine Instanz der Klasse `Cat`.

Und um `fluffy` zu erzeugen, rufen Sie `Cat` auf.

Eine Python-Klasse ist also auch ein **Callable**.

Darum können Sie in **ReadyAPI** auch eine Python-Klasse als Abhängigkeit verwenden.

Was ReadyAPI tatsächlich prüft, ist, ob es sich um ein „Callable“ (Funktion, Klasse oder irgendetwas anderes) handelt und ob die Parameter definiert sind.

Wenn Sie **ReadyAPI** ein „Callable“ als Abhängigkeit übergeben, analysiert es die Parameter dieses „Callables“ und verarbeitet sie auf die gleiche Weise wie die Parameter einer *Pfadoperation-Funktion*. Einschließlich Unterabhängigkeiten.

Das gilt auch für Callables ohne Parameter. So wie es auch für *Pfadoperation-Funktionen* ohne Parameter gilt.

Dann können wir das „Dependable“ `common_parameters` der Abhängigkeit von oben in die Klasse `CommonQueryParams` ändern:

{* ../../examples/dependencies/tutorial002_an_py310.py hl[11:15] *}

Achten Sie auf die Methode `__init__`, die zum Erstellen der Instanz der Klasse verwendet wird:

{* ../../examples/dependencies/tutorial002_an_py310.py hl[12] *}

... sie hat die gleichen Parameter wie unsere vorherige `common_parameters`:

{* ../../examples/dependencies/tutorial001_an_py310.py hl[8] *}

Diese Parameter werden von **ReadyAPI** verwendet, um die Abhängigkeit „aufzulösen“.

In beiden Fällen wird sie haben:

* Einen optionalen `q`-Query-Parameter, der ein `str` ist.
* Einen `skip`-Query-Parameter, der ein `int` ist, mit einem Defaultwert `0`.
* Einen `limit`-Query-Parameter, der ein `int` ist, mit einem Defaultwert `100`.

In beiden Fällen werden die Daten konvertiert, validiert, im OpenAPI-Schema dokumentiert, usw.

## Verwendung

Jetzt können Sie Ihre Abhängigkeit mithilfe dieser Klasse deklarieren.

{* ../../examples/dependencies/tutorial002_an_py310.py hl[19] *}

**ReadyAPI** ruft die Klasse `CommonQueryParams` auf. Dadurch wird eine „Instanz“ dieser Klasse erstellt und die Instanz wird als Parameter `commons` an Ihre Funktion überreicht.

## Typannotation vs. `Depends`

Beachten Sie, wie wir `CommonQueryParams` im obigen Code zweimal schreiben:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

Das letzte `CommonQueryParams`, in:

```Python
... Depends(CommonQueryParams)
```

... ist das, was **ReadyAPI** tatsächlich verwendet, um die Abhängigkeit zu ermitteln.

Aus diesem extrahiert ReadyAPI die deklarierten Parameter, und dieses ist es, was ReadyAPI auch aufruft.

---

In diesem Fall hat das erste `CommonQueryParams` in:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, ...
```

////

//// tab | Python 3.8+ nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons: CommonQueryParams ...
```

////

... keine besondere Bedeutung für **ReadyAPI**. ReadyAPI verwendet es nicht für die Datenkonvertierung, -validierung, usw. (da es dafür `Depends(CommonQueryParams)` verwendet).

Sie könnten tatsächlich einfach schreiben:

//// tab | Python 3.8+

```Python
commons: Annotated[Any, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons = Depends(CommonQueryParams)
```

////

... wie in:

{* ../../examples/dependencies/tutorial003_an_py310.py hl[19] *}

Es wird jedoch empfohlen, den Typ zu deklarieren, da Ihr Editor so weiß, was als Parameter `commons` übergeben wird, und Ihnen dann bei der Codevervollständigung, Typprüfungen, usw. helfen kann:

<img src="/img/tutorial/dependencies/image02.png">

## Abkürzung

Aber Sie sehen, dass wir hier etwas Codeduplizierung haben, indem wir `CommonQueryParams` zweimal schreiben:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

**ReadyAPI** bietet eine Abkürzung für diese Fälle, wo die Abhängigkeit *speziell* eine Klasse ist, welche **ReadyAPI** aufruft, um eine Instanz der Klasse selbst zu erstellen.

In diesem speziellen Fall können Sie Folgendes tun:

Anstatt zu schreiben:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

... schreiben Sie:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends()]
```

////

//// tab | Python 3.8 nicht annotiert

/// tip | Tipp

Bevorzugen Sie die `Annotated`-Version, falls möglich.

///

```Python
commons: CommonQueryParams = Depends()
```

////

Sie deklarieren die Abhängigkeit als Typ des Parameters und verwenden `Depends()` ohne Parameter, anstatt die vollständige Klasse *erneut* in `Depends(CommonQueryParams)` schreiben zu müssen.

Dasselbe Beispiel würde dann so aussehen:

{* ../../examples/dependencies/tutorial004_an_py310.py hl[19] *}

... und **ReadyAPI** wird wissen, was zu tun ist.

/// tip | Tipp

Wenn Sie das eher verwirrt, als Ihnen zu helfen, ignorieren Sie es, Sie *brauchen* es nicht.

Es ist nur eine Abkürzung. Es geht **ReadyAPI** darum, Ihnen dabei zu helfen, Codeverdoppelung zu minimieren.

///
