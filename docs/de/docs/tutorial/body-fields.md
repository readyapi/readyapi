# Body – Felder

So wie Sie zusätzliche Validation und Metadaten in Parametern der **Pfadoperation-Funktion** mittels `Query`, `Path` und `Body` deklarieren, können Sie auch innerhalb von Pydantic-Modellen zusätzliche Validation und Metadaten deklarieren, mittels Pydantics `Field`.

## `Field` importieren

Importieren Sie es zuerst:

{* ../../examples/body_fields/tutorial001_an_py310.py hl[4] *}

/// warning | Achtung

Beachten Sie, dass `Field` direkt von `pydantic` importiert wird, nicht von `readyapi`, wie die anderen (`Query`, `Path`, `Body`, usw.)

///

## Modellattribute deklarieren

Dann können Sie `Field` mit Modellattributen deklarieren:

{* ../../examples/body_fields/tutorial001_an_py310.py hl[11:14] *}

`Field` funktioniert genauso wie `Query`, `Path` und `Body`, es hat die gleichen Parameter, usw.

/// note | Technische Details

Tatsächlich erstellen `Query`, `Path` und andere, die sie kennenlernen werden, Instanzen von Unterklassen einer allgemeinen Klasse `Param`, die ihrerseits eine Unterklasse von Pydantics `FieldInfo`-Klasse ist.

Und Pydantics `Field` gibt ebenfalls eine Instanz von `FieldInfo` zurück.

`Body` gibt auch Instanzen einer Unterklasse von `FieldInfo` zurück. Und später werden Sie andere sehen, die Unterklassen der `Body`-Klasse sind.

Denken Sie daran, dass `Query`, `Path` und andere von `readyapi` tatsächlich Funktionen sind, die spezielle Klassen zurückgeben.

///

/// tip | Tipp

Beachten Sie, dass jedes Modellattribut mit einem Typ, Defaultwert und `Field` die gleiche Struktur hat wie ein Parameter einer Pfadoperation-Funktion, nur mit `Field` statt `Path`, `Query`, `Body`.

///

## Zusätzliche Information hinzufügen

Sie können zusätzliche Information in `Field`, `Query`, `Body`, usw. deklarieren. Und es wird im generierten JSON-Schema untergebracht.

Sie werden später mehr darüber lernen, wie man zusätzliche Information unterbringt, wenn Sie lernen, Beispiele zu deklarieren.

/// warning | Achtung

Extra-Schlüssel, die `Field` überreicht werden, werden auch im resultierenden OpenAPI-Schema Ihrer Anwendung gelistet. Da diese Schlüssel nicht notwendigerweise Teil der OpenAPI-Spezifikation sind, könnten einige OpenAPI-Tools, wie etwa [der OpenAPI-Validator](https://validator.swagger.io/), nicht mit Ihrem generierten Schema funktionieren.

///

## Zusammenfassung

Sie können Pydantics `Field` verwenden, um zusätzliche Validierungen und Metadaten für Modellattribute zu deklarieren.

Sie können auch Extra-Schlüssel verwenden, um zusätzliche JSON-Schema-Metadaten zu überreichen.
