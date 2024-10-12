# OpenAPI-Callbacks

Sie könnten eine API mit einer _Pfadoperation_ erstellen, die einen Request an eine _externe API_ auslösen könnte, welche von jemand anderem erstellt wurde (wahrscheinlich derselbe Entwickler, der Ihre API _verwenden_ würde).

Der Vorgang, der stattfindet, wenn Ihre API-Anwendung die _externe API_ aufruft, wird als „Callback“ („Rückruf“) bezeichnet. Denn die Software, die der externe Entwickler geschrieben hat, sendet einen Request an Ihre API und dann _ruft Ihre API zurück_ (_calls back_) und sendet einen Request an eine _externe API_ (die wahrscheinlich vom selben Entwickler erstellt wurde).

In diesem Fall möchten Sie möglicherweise dokumentieren, wie diese externe API aussehen _sollte_. Welche _Pfadoperation_ sie haben sollte, welchen Body sie erwarten sollte, welche Response sie zurückgeben sollte, usw.

## Eine Anwendung mit Callbacks

Sehen wir uns das alles anhand eines Beispiels an.

Stellen Sie sich vor, Sie entwickeln eine Anwendung, mit der Sie Rechnungen erstellen können.

Diese Rechnungen haben eine `id`, einen optionalen `title`, einen `customer` (Kunde) und ein `total` (Gesamtsumme).

Der Benutzer Ihrer API (ein externer Entwickler) erstellt mit einem POST-Request eine Rechnung in Ihrer API.

Dann wird Ihre API (beispielsweise):

- die Rechnung an einen Kunden des externen Entwicklers senden.
- das Geld einsammeln.
- eine Benachrichtigung an den API-Benutzer (den externen Entwickler) zurücksenden.
  - Dies erfolgt durch Senden eines POST-Requests (von _Ihrer API_) an eine _externe API_, die von diesem externen Entwickler bereitgestellt wird (das ist der „Callback“).

## Die normale **ReadyAPI**-Anwendung

Sehen wir uns zunächst an, wie die normale API-Anwendung aussehen würde, bevor wir den Callback hinzufügen.

Sie verfügt über eine _Pfadoperation_, die einen `Invoice`-Body empfängt, und einen Query-Parameter `callback_url`, der die URL für den Callback enthält.

Dieser Teil ist ziemlich normal, der größte Teil des Codes ist Ihnen wahrscheinlich bereits bekannt:

```Python hl_lines="9-13  36-53"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

/// tip | "Tipp"

Der Query-Parameter `callback_url` verwendet einen Pydantic-<a href="https://docs.pydantic.dev/latest/api/networks/" class="external-link" target="_blank">Url</a>-Typ.

///

Das einzig Neue ist `callbacks=invoices_callback_router.routes` als Argument für den _Pfadoperation-Dekorator_. Wir werden als Nächstes sehen, was das ist.

## Dokumentation des Callbacks

Der tatsächliche Callback-Code hängt stark von Ihrer eigenen API-Anwendung ab.

Und er wird wahrscheinlich von Anwendung zu Anwendung sehr unterschiedlich sein.

Es könnten nur eine oder zwei Codezeilen sein, wie zum Beispiel:

```Python
callback_url = "https://example.com/api/v1/invoices/events/"
httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})
```

Der möglicherweise wichtigste Teil des Callbacks besteht jedoch darin, sicherzustellen, dass Ihr API-Benutzer (der externe Entwickler) die _externe API_ gemäß den Daten, die _Ihre API_ im Requestbody des Callbacks senden wird, korrekt implementiert, usw.

Als Nächstes fügen wir den Code hinzu, um zu dokumentieren, wie diese _externe API_ aussehen sollte, um den Callback von _Ihrer API_ zu empfangen.

Diese Dokumentation wird in der Swagger-Oberfläche unter `/docs` in Ihrer API angezeigt und zeigt externen Entwicklern, wie diese die _externe API_ erstellen sollten.

In diesem Beispiel wird nicht der Callback selbst implementiert (das könnte nur eine Codezeile sein), sondern nur der Dokumentationsteil.

/// tip | "Tipp"

Der eigentliche Callback ist nur ein HTTP-Request.

Wenn Sie den Callback selbst implementieren, können Sie beispielsweise <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a> oder <a href="https://requests.readthedocs.io/" class="external-link" target="_blank">Requests</a> verwenden.

///

## Schreiben des Codes, der den Callback dokumentiert

Dieser Code wird nicht in Ihrer Anwendung ausgeführt, wir benötigen ihn nur, um zu _dokumentieren_, wie diese _externe API_ aussehen soll.

Sie wissen jedoch bereits, wie Sie mit **ReadyAPI** ganz einfach eine automatische Dokumentation für eine API erstellen.

Daher werden wir dasselbe Wissen nutzen, um zu dokumentieren, wie die _externe API_ aussehen sollte ... indem wir die _Pfadoperation(en)_ erstellen, welche die externe API implementieren soll (die, welche Ihre API aufruft).

/// tip | "Tipp"

Wenn Sie den Code zum Dokumentieren eines Callbacks schreiben, kann es hilfreich sein, sich vorzustellen, dass Sie dieser _externe Entwickler_ sind. Und dass Sie derzeit die _externe API_ implementieren, nicht _Ihre API_.

Wenn Sie diese Sichtweise (des _externen Entwicklers_) vorübergehend übernehmen, wird es offensichtlicher, wo die Parameter, das Pydantic-Modell für den Body, die Response, usw. für diese _externe API_ hingehören.

///

### Einen Callback-`APIRouter` erstellen

Erstellen Sie zunächst einen neuen `APIRouter`, der einen oder mehrere Callbacks enthält.

```Python hl_lines="3  25"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

### Die Callback-_Pfadoperation_ erstellen

Um die Callback-_Pfadoperation_ zu erstellen, verwenden Sie denselben `APIRouter`, den Sie oben erstellt haben.

Sie sollte wie eine normale ReadyAPI-_Pfadoperation_ aussehen:

- Sie sollte wahrscheinlich eine Deklaration des Bodys enthalten, die sie erhalten soll, z. B. `body: InvoiceEvent`.
- Und sie könnte auch eine Deklaration der Response enthalten, die zurückgegeben werden soll, z. B. `response_model=InvoiceEventReceived`.

```Python hl_lines="16-18  21-22  28-32"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

Es gibt zwei Hauptunterschiede zu einer normalen _Pfadoperation_:

- Es muss kein tatsächlicher Code vorhanden sein, da Ihre Anwendung diesen Code niemals aufruft. Sie wird nur zur Dokumentation der _externen API_ verwendet. Die Funktion könnte also einfach `pass` enthalten.
- Der _Pfad_ kann einen <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression" class="external-link" target="_blank">OpenAPI-3-Ausdruck</a> enthalten (mehr dazu weiter unten), wo er Variablen mit Parametern und Teilen des ursprünglichen Requests verwenden kann, der an _Ihre API_ gesendet wurde.

### Der Callback-Pfadausdruck

Der Callback-_Pfad_ kann einen <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression" class="external-link" target="_blank">OpenAPI-3-Ausdruck</a> enthalten, welcher Teile des ursprünglichen Requests enthalten kann, der an _Ihre API_ gesendet wurde.

In diesem Fall ist es der `str`:

```Python
"{$callback_url}/invoices/{$request.body.id}"
```

Wenn Ihr API-Benutzer (der externe Entwickler) also einen Request an _Ihre API_ sendet, via:

```
https://yourapi.com/invoices/?callback_url=https://www.external.org/events
```

mit einem JSON-Körper:

```JSON
{
    "id": "2expen51ve",
    "customer": "Mr. Richie Rich",
    "total": "9999"
}
```

dann verarbeitet _Ihre API_ die Rechnung und sendet irgendwann später einen Callback-Request an die `callback_url` (die _externe API_):

```
https://www.external.org/events/invoices/2expen51ve
```

mit einem JSON-Body, der etwa Folgendes enthält:

```JSON
{
    "description": "Payment celebration",
    "paid": true
}
```

und sie würde eine Response von dieser _externen API_ mit einem JSON-Body wie dem folgenden erwarten:

```JSON
{
    "ok": true
}
```

/// tip | "Tipp"

Beachten Sie, dass die verwendete Callback-URL die URL enthält, die als Query-Parameter in `callback_url` (`https://www.external.org/events`) empfangen wurde, und auch die Rechnungs-`id` aus dem JSON-Body (`2expen51ve`).

///

### Den Callback-Router hinzufügen

An diesem Punkt haben Sie die benötigte(n) _Callback-Pfadoperation(en)_ (diejenige(n), die der _externe Entwickler_ in der _externen API_ implementieren sollte) im Callback-Router, den Sie oben erstellt haben.

Verwenden Sie nun den Parameter `callbacks` im _Pfadoperation-Dekorator Ihrer API_, um das Attribut `.routes` (das ist eigentlich nur eine `list`e von Routen/_Pfadoperationen_) dieses Callback-Routers zu übergeben:

```Python hl_lines="35"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

/// tip | "Tipp"

Beachten Sie, dass Sie nicht den Router selbst (`invoices_callback_router`) an `callback=` übergeben, sondern das Attribut `.routes`, wie in `invoices_callback_router.routes`.

///

### Es in der Dokumentation ansehen

Jetzt können Sie Ihre Anwendung mit Uvicorn starten und auf <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> gehen.

Sie sehen Ihre Dokumentation, einschließlich eines Abschnitts „Callbacks“ für Ihre _Pfadoperation_, der zeigt, wie die _externe API_ aussehen sollte:

<img src="/img/tutorial/openapi-callbacks/image01.png">
