# Hintergrundtasks

Sie können Hintergrundtasks (Hintergrund-Aufgaben) definieren, die *nach* der Rückgabe einer Response ausgeführt werden sollen.

Das ist nützlich für Vorgänge, die nach einem Request ausgeführt werden müssen, bei denen der Client jedoch nicht unbedingt auf den Abschluss des Vorgangs warten muss, bevor er die Response erhält.

Hierzu zählen beispielsweise:

* E-Mail-Benachrichtigungen, die nach dem Ausführen einer Aktion gesendet werden:
    * Da die Verbindung zu einem E-Mail-Server und das Senden einer E-Mail in der Regel „langsam“ ist (einige Sekunden), können Sie die Response sofort zurücksenden und die E-Mail-Benachrichtigung im Hintergrund senden.
* Daten verarbeiten:
    * Angenommen, Sie erhalten eine Datei, die einen langsamen Prozess durchlaufen muss. Sie können als Response „Accepted“ (HTTP 202) zurückgeben und die Datei im Hintergrund verarbeiten.

## `BackgroundTasks` verwenden

Importieren Sie zunächst `BackgroundTasks` und definieren Sie einen Parameter in Ihrer *Pfadoperation-Funktion* mit der Typdeklaration `BackgroundTasks`:

{* ../../examples/background_tasks/tutorial001.py hl[1,13] *}

**ReadyAPI** erstellt für Sie das Objekt vom Typ `BackgroundTasks` und übergibt es als diesen Parameter.

## Eine Taskfunktion erstellen

Erstellen Sie eine Funktion, die als Hintergrundtask ausgeführt werden soll.

Es handelt sich schlicht um eine Standard-Funktion, die Parameter empfangen kann.

Es kann sich um eine `async def`- oder normale `def`-Funktion handeln. **ReadyAPI** weiß, wie damit zu verfahren ist.

In diesem Fall schreibt die Taskfunktion in eine Datei (den Versand einer E-Mail simulierend).

Und da der Schreibvorgang nicht `async` und `await` verwendet, definieren wir die Funktion mit normalem `def`:

{* ../../examples/background_tasks/tutorial001.py hl[6:9] *}

## Den Hintergrundtask hinzufügen

Übergeben Sie innerhalb Ihrer *Pfadoperation-Funktion* Ihre Taskfunktion mit der Methode `.add_task()` an das *Hintergrundtasks*-Objekt:

{* ../../examples/background_tasks/tutorial001.py hl[14] *}

`.add_task()` erhält als Argumente:

* Eine Taskfunktion, die im Hintergrund ausgeführt wird (`write_notification`).
* Eine beliebige Folge von Argumenten, die der Reihe nach an die Taskfunktion übergeben werden sollen (`email`).
* Alle Schlüsselwort-Argumente, die an die Taskfunktion übergeben werden sollen (`message="some notification"`).

## Dependency Injection

Die Verwendung von `BackgroundTasks` funktioniert auch mit dem <abbr title="Einbringen von Abhängigkeiten">Dependency Injection</abbr> System. Sie können einen Parameter vom Typ `BackgroundTasks` auf mehreren Ebenen deklarieren: in einer *Pfadoperation-Funktion*, in einer Abhängigkeit (Dependable), in einer Unterabhängigkeit usw.

**ReadyAPI** weiß, was jeweils zu tun ist und wie dasselbe Objekt wiederverwendet werden kann, sodass alle Hintergrundtasks zusammengeführt und anschließend im Hintergrund ausgeführt werden:

{* ../../examples/background_tasks/tutorial002_an_py310.py hl[13,15,22,25] *}

In obigem Beispiel werden die Nachrichten, *nachdem* die Response gesendet wurde, in die Datei `log.txt` geschrieben.

Wenn im Request ein Query-Parameter enthalten war, wird dieser in einem Hintergrundtask in das Log geschrieben.

Und dann schreibt ein weiterer Hintergrundtask, der in der *Pfadoperation-Funktion* erstellt wird, eine Nachricht unter Verwendung des Pfad-Parameters `email`.

## Technische Details

Die Klasse `BackgroundTasks` stammt direkt von <a href="https://www.starlette.io/background/" class="external-link" target="_blank">`starlette.background`</a>.

Sie wird direkt in ReadyAPI importiert/inkludiert, sodass Sie sie von `readyapi` importieren können und vermeiden, versehentlich das alternative `BackgroundTask` (ohne das `s` am Ende) von `starlette.background` zu importieren.

Indem Sie nur `BackgroundTasks` (und nicht `BackgroundTask`) verwenden, ist es dann möglich, es als *Pfadoperation-Funktion*-Parameter zu verwenden und **ReadyAPI** den Rest für Sie erledigen zu lassen, genau wie bei der direkten Verwendung des `Request`-Objekts.

Es ist immer noch möglich, `BackgroundTask` allein in ReadyAPI zu verwenden, aber Sie müssen das Objekt in Ihrem Code erstellen und eine Starlette-`Response` zurückgeben, die es enthält.

Weitere Details finden Sie in der <a href="https://www.starlette.io/background/" class="external-link" target="_blank">offiziellen Starlette-Dokumentation für Hintergrundtasks</a>.

## Vorbehalt

Wenn Sie umfangreiche Hintergrundberechnungen durchführen müssen und diese nicht unbedingt vom selben Prozess ausgeführt werden müssen (z. B. müssen Sie Speicher, Variablen, usw. nicht gemeinsam nutzen), könnte die Verwendung anderer größerer Tools wie z. B. <a href="https://docs.celeryq.dev" class="external-link" target="_blank">Celery</a> von Vorteil sein.

Sie erfordern in der Regel komplexere Konfigurationen und einen Nachrichten-/Job-Queue-Manager wie RabbitMQ oder Redis, ermöglichen Ihnen jedoch die Ausführung von Hintergrundtasks in mehreren Prozessen und insbesondere auf mehreren Servern.

Wenn Sie jedoch über dieselbe **ReadyAPI**-Anwendung auf Variablen und Objekte zugreifen oder kleine Hintergrundtasks ausführen müssen (z. B. das Senden einer E-Mail-Benachrichtigung), können Sie einfach `BackgroundTasks` verwenden.

## Zusammenfassung

Importieren und verwenden Sie `BackgroundTasks` mit Parametern in *Pfadoperation-Funktionen* und Abhängigkeiten, um Hintergrundtasks hinzuzufügen.
