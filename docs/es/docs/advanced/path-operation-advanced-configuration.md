# Configuración avanzada de las operaciones de path

## OpenAPI operationId

/// warning | "Advertencia"

Si no eres una persona "experta" en OpenAPI, probablemente no necesitas leer esto.

///

Puedes asignar el `operationId` de OpenAPI para ser usado en tu _operación de path_ con el parámetro `operation_id`.

En este caso tendrías que asegurarte de que sea único para cada operación.

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial001.py!}
```

### Usando el nombre de la _función de la operación de path_ en el operationId

Si quieres usar tus nombres de funciones de API como `operationId`s, puedes iterar sobre todos ellos y sobrescribir `operation_id` de cada _operación de path_ usando su `APIRoute.name`.

Deberías hacerlo después de adicionar todas tus _operaciones de path_.

```Python hl_lines="2 12 13 14 15 16 17 18 19 20 21 24"
{!../../docs_src/path_operation_advanced_configuration/tutorial002.py!}
```

/// tip | Consejo

Si llamas manualmente a `app.openapi()`, debes actualizar el `operationId`s antes de hacerlo.

///

/// warning | Advertencia

Si haces esto, debes asegurarte de que cada una de tus _funciones de las operaciones de path_ tenga un nombre único.

Incluso si están en diferentes módulos (archivos Python).

///

## Excluir de OpenAPI

Para excluir una _operación de path_ del esquema OpenAPI generado (y por tanto del la documentación generada automáticamente), usa el parámetro `include_in_schema` y asigna el valor como `False`;

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial003.py!}
```

## Descripción avanzada desde el docstring

Puedes limitar las líneas usadas desde el docstring de una _operación de path_ para OpenAPI.

Agregar un `\f` (un carácter de "form feed" escapado) hace que **ReadyAPI** trunque el output utilizada para OpenAPI en ese punto.

No será mostrado en la documentación, pero otras herramientas (como Sphinx) serán capaces de usar el resto.

```Python hl_lines="19 20 21 22 23 24 25 26 27 28 29"
{!../../docs_src/path_operation_advanced_configuration/tutorial004.py!}
```
