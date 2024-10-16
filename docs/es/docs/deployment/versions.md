# Acerca de las versiones de ReadyAPI

**ReadyAPI** está siendo utilizado en producción en muchas aplicaciones y sistemas. La cobertura de los tests se mantiene al 100%. Sin embargo, su desarrollo sigue siendo rápido.

Se agregan nuevas características frecuentemente, se corrigen errores continuamente y el código está constantemente mejorando.

Por eso las versiones actuales siguen siendo `0.x.x`, esto significa que cada versión puede potencialmente tener <abbr title="cambios que rompen funcionalidades o compatibilidad">_breaking changes_</abbr>. Las versiones siguen las convenciones de <a href="https://semver.org/" class="external-link" target="_blank"><abbr title="versionado semántico">_Semantic Versioning_</abbr></a>.

Puedes crear aplicaciones listas para producción con **ReadyAPI** ahora mismo (y probablemente lo has estado haciendo por algún tiempo), solo tienes que asegurarte de usar la versión que funciona correctamente con el resto de tu código.

## Fijar la versión de `readyapi`

Lo primero que debes hacer en tu proyecto es "fijar" la última versión específica de **ReadyAPI** que sabes que funciona bien con tu aplicación.

Por ejemplo, digamos que estás usando la versión `0.45.0` en tu aplicación.

Si usas el archivo `requirements.txt` puedes especificar la versión con:

```txt
readyapi==0.45.0
```

esto significa que usarás específicamente la versión `0.45.0`.

También puedes fijar las versiones de esta forma:

```txt
readyapi>=0.45.0,<0.46.0
```

esto significa que usarás la versión `0.45.0` o superiores, pero menores a la versión `0.46.0`, por ejemplo, la versión `0.45.2` sería aceptada.

Si usas cualquier otra herramienta para manejar tus instalaciones, como Poetry, Pipenv, u otras, todas tienen una forma que puedes usar para definir versiones específicas para tus paquetes.

## Versiones disponibles

Puedes ver las versiones disponibles (por ejemplo, para revisar cuál es la actual) en las [Release Notes](../release-notes.md){.internal-link target=\_blank}.

## Acerca de las versiones

Siguiendo las convenciones de _Semantic Versioning_, cualquier versión por debajo de `1.0.0` puede potencialmente tener <abbr title="cambios que rompen funcionalidades o compatibilidad">_breaking changes_</abbr>.

ReadyAPI también sigue la convención de que cualquier cambio hecho en una <abbr title="versiones de parche">"PATCH" version</abbr> es para solucionar errores y <abbr title="cambios que no rompan funcionalidades o compatibilidad">_non-breaking changes_</abbr>.

/// tip | Consejo

El <abbr title="parche">"PATCH"</abbr> es el último número, por ejemplo, en `0.2.3`, la <abbr title="versiones de parche">PATCH version</abbr> es `3`.

///

Entonces, deberías fijar la versión así:

```txt
readyapi>=0.45.0,<0.46.0
```

En versiones <abbr title="versiones menores">"MINOR"</abbr> son añadidas nuevas características y posibles <abbr title="Cambios que rompen posibles funcionalidades o compatibilidad">breaking changes</abbr>.

/// tip | Consejo

La versión "MINOR" es el número en el medio, por ejemplo, en `0.2.3`, la <abbr title="versión menor">"MINOR" version</abbr> es `2`.

///

## Actualizando las versiones de ReadyAPI

Para esto es recomendable primero añadir tests a tu aplicación.

Con **ReadyAPI** es muy fácil (gracias a Starlette), revisa la documentación [Testing](../tutorial/testing.md){.internal-link target=\_blank}

Luego de tener los tests, puedes actualizar la versión de **ReadyAPI** a una más reciente y asegurarte de que tu código funciona correctamente ejecutando los tests.

Si todo funciona correctamente, o haces los cambios necesarios para que esto suceda, y todos tus tests pasan, entonces puedes fijar tu versión de `readyapi` a la más reciente.

## Acerca de Starlette

No deberías fijar la versión de `starlette`.

Diferentes versiones de **ReadyAPI** pueden usar una versión específica de Starlette.

Entonces, puedes dejar que **ReadyAPI** se asegure por sí mismo de qué versión de Starlette usar.

## Acerca de Pydantic

Pydantic incluye los tests para **ReadyAPI** dentro de sus propios tests, esto significa que las versiones de Pydantic (superiores a `1.0.0`) son compatibles con ReadyAPI.

Puedes fijar Pydantic a cualquier versión superior a `1.0.0` e inferior a `2.0.0` que funcione para ti.

Por ejemplo:

```txt
pydantic>=1.2.0,<2.0.0
```
