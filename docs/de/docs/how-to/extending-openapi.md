# OpenAPI erweitern

In einigen Fällen müssen Sie möglicherweise das generierte OpenAPI-Schema ändern.

In diesem Abschnitt erfahren Sie, wie.

## Der normale Vorgang

Der normale (Standard-)Prozess ist wie folgt.

Eine `ReadyAPI`-Anwendung (-Instanz) verfügt über eine `.openapi()`-Methode, von der erwartet wird, dass sie das OpenAPI-Schema zurückgibt.

Als Teil der Erstellung des Anwendungsobjekts wird eine *Pfadoperation* für `/openapi.json` (oder welcher Wert für den Parameter `openapi_url` gesetzt wurde) registriert.

Diese gibt lediglich eine JSON-Response zurück, mit dem Ergebnis der Methode `.openapi()` der Anwendung.

Standardmäßig überprüft die Methode `.openapi()` die Eigenschaft `.openapi_schema`, um zu sehen, ob diese Inhalt hat, und gibt diesen zurück.

Ist das nicht der Fall, wird der Inhalt mithilfe der Hilfsfunktion unter `readyapi.openapi.utils.get_openapi` generiert.

Und diese Funktion `get_openapi()` erhält als Parameter:

* `title`: Der OpenAPI-Titel, der in der Dokumentation angezeigt wird.
* `version`: Die Version Ihrer API, z. B. `2.5.0`.
* `openapi_version`: Die Version der verwendeten OpenAPI-Spezifikation. Standardmäßig die neueste Version: `3.1.0`.
* `summary`: Eine kurze Zusammenfassung der API.
* `description`: Die Beschreibung Ihrer API. Dies kann Markdown enthalten und wird in der Dokumentation angezeigt.
* `routes`: Eine Liste von Routen, dies sind alle registrierten *Pfadoperationen*. Sie stammen von `app.routes`.

/// info

Der Parameter `summary` ist in OpenAPI 3.1.0 und höher verfügbar und wird von ReadyAPI 0.99.0 und höher unterstützt.

///

## Überschreiben der Standardeinstellungen

Mithilfe der oben genannten Informationen können Sie dieselbe Hilfsfunktion verwenden, um das OpenAPI-Schema zu generieren und jeden benötigten Teil zu überschreiben.

Fügen wir beispielsweise <a href="https://github.com/Rebilly/ReDoc/blob/master/docs/redoc-vendor-extensions.md#x-logo" class="external-link" target="_blank">ReDocs OpenAPI-Erweiterung</a> zum Einbinden eines benutzerdefinierten Logos hinzu.

### Normales **ReadyAPI**

Schreiben Sie zunächst wie gewohnt Ihre ganze **ReadyAPI**-Anwendung:

{* ../../examples/extending_openapi/tutorial001.py hl[1,4,7:9] *}

### Das OpenAPI-Schema generieren

Verwenden Sie dann dieselbe Hilfsfunktion, um das OpenAPI-Schema innerhalb einer `custom_openapi()`-Funktion zu generieren:

{* ../../examples/extending_openapi/tutorial001.py hl[2,15:21] *}

### Das OpenAPI-Schema ändern

Jetzt können Sie die ReDoc-Erweiterung hinzufügen und dem `info`-„Objekt“ im OpenAPI-Schema ein benutzerdefiniertes `x-logo` hinzufügen:

{* ../../examples/extending_openapi/tutorial001.py hl[22:24] *}

### Zwischenspeichern des OpenAPI-Schemas

Sie können die Eigenschaft `.openapi_schema` als „Cache“ verwenden, um Ihr generiertes Schema zu speichern.

Auf diese Weise muss Ihre Anwendung das Schema nicht jedes Mal generieren, wenn ein Benutzer Ihre API-Dokumentation öffnet.

Es wird nur einmal generiert und dann wird dasselbe zwischengespeicherte Schema für die nächsten Requests verwendet.

{* ../../examples/extending_openapi/tutorial001.py hl[13:14,25:26] *}

### Die Methode überschreiben

Jetzt können Sie die Methode `.openapi()` durch Ihre neue Funktion ersetzen.

{* ../../examples/extending_openapi/tutorial001.py hl[29] *}

### Testen

Sobald Sie auf <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> gehen, werden Sie sehen, dass Ihr benutzerdefiniertes Logo verwendet wird (in diesem Beispiel das Logo von **ReadyAPI**):

<img src="/img/tutorial/extending-openapi/image01.png">
