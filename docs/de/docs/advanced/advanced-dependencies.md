# Fortgeschrittene Abhängigkeiten

## Parametrisierte Abhängigkeiten

Alle Abhängigkeiten, die wir bisher gesehen haben, waren festgelegte Funktionen oder Klassen.

Es kann jedoch Fälle geben, in denen Sie Parameter für eine Abhängigkeit festlegen möchten, ohne viele verschiedene Funktionen oder Klassen zu deklarieren.

Stellen wir uns vor, wir möchten eine Abhängigkeit haben, die prüft, ob ein Query-Parameter `q` einen vordefinierten Inhalt hat.

Aber wir wollen diesen vordefinierten Inhalt per Parameter festlegen können.

## Eine „aufrufbare“ Instanz

In Python gibt es eine Möglichkeit, eine Instanz einer Klasse „aufrufbar“ („callable“) zu machen.

Nicht die Klasse selbst (die bereits aufrufbar ist), sondern eine Instanz dieser Klasse.

Dazu deklarieren wir eine Methode `__call__`:

{* ../../examples/dependencies/tutorial011_an_py39.py hl[12] *}

In diesem Fall ist dieses `__call__` das, was **ReadyAPI** verwendet, um nach zusätzlichen Parametern und Unterabhängigkeiten zu suchen, und das ist es auch, was später aufgerufen wird, um einen Wert an den Parameter in Ihrer *Pfadoperation-Funktion* zu übergeben.

## Die Instanz parametrisieren

Und jetzt können wir `__init__` verwenden, um die Parameter der Instanz zu deklarieren, die wir zum `Parametrisieren` der Abhängigkeit verwenden können:

{* ../../examples/dependencies/tutorial011_an_py39.py hl[9] *}

In diesem Fall wird **ReadyAPI** `__init__` nie berühren oder sich darum kümmern, wir werden es direkt in unserem Code verwenden.

## Eine Instanz erstellen

Wir könnten eine Instanz dieser Klasse erstellen mit:

{* ../../examples/dependencies/tutorial011_an_py39.py hl[18] *}

Und auf diese Weise können wir unsere Abhängigkeit „parametrisieren“, die jetzt `"bar"` enthält, als das Attribut `checker.fixed_content`.

## Die Instanz als Abhängigkeit verwenden

Dann könnten wir diesen `checker` in einem `Depends(checker)` anstelle von `Depends(FixedContentQueryChecker)` verwenden, da die Abhängigkeit die Instanz `checker` und nicht die Klasse selbst ist.

Und beim Auflösen der Abhängigkeit ruft **ReadyAPI** diesen `checker` wie folgt auf:

```Python
checker(q="somequery")
```

... und übergibt, was immer das als Wert dieser Abhängigkeit in unserer *Pfadoperation-Funktion* zurückgibt, als den Parameter `fixed_content_included`:

{* ../../examples/dependencies/tutorial011_an_py39.py hl[22] *}

/// tip | Tipp

Das alles mag gekünstelt wirken. Und es ist möglicherweise noch nicht ganz klar, welchen Nutzen das hat.

Diese Beispiele sind bewusst einfach gehalten, zeigen aber, wie alles funktioniert.

In den Kapiteln zum Thema Sicherheit gibt es Hilfsfunktionen, die auf die gleiche Weise implementiert werden.

Wenn Sie das hier alles verstanden haben, wissen Sie bereits, wie diese Sicherheits-Hilfswerkzeuge unter der Haube funktionieren.

///
