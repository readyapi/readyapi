# Sicherheitstools

Wenn Sie Abhängigkeiten mit OAuth2-Scopes deklarieren müssen, verwenden Sie `Security()`.

Aber Sie müssen immer noch definieren, was das <abbr title="Das von dem abhängt, die zu verwendende Abhängigkeit">Dependable</abbr>, das Callable ist, welches Sie als Parameter an `Depends()` oder `Security()` übergeben.

Es gibt mehrere Tools, mit denen Sie diese Dependables erstellen können, und sie werden in OpenAPI integriert, sodass sie in der Oberfläche der automatischen Dokumentation angezeigt werden und von automatisch generierten Clients und SDKs, usw., verwendet werden können.

Sie können sie von `readyapi.security` importieren:

```python
from readyapi.security import (
    APIKeyCookie,
    APIKeyHeader,
    APIKeyQuery,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPDigest,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    OAuth2PasswordRequestFormStrict,
    OpenIdConnect,
    SecurityScopes,
)
```

## API-Schlüssel-Sicherheitsschemas

::: readyapi.security.APIKeyCookie

::: readyapi.security.APIKeyHeader

::: readyapi.security.APIKeyQuery

## HTTP-Authentifizierungsschemas

::: readyapi.security.HTTPBasic

::: readyapi.security.HTTPBearer

::: readyapi.security.HTTPDigest

## HTTP-Anmeldeinformationen

::: readyapi.security.HTTPAuthorizationCredentials

::: readyapi.security.HTTPBasicCredentials

## OAuth2-Authentifizierung

::: readyapi.security.OAuth2

::: readyapi.security.OAuth2AuthorizationCodeBearer

::: readyapi.security.OAuth2PasswordBearer

## OAuth2-Passwortformulare

::: readyapi.security.OAuth2PasswordRequestForm

::: readyapi.security.OAuth2PasswordRequestFormStrict

## OAuth2-Sicherheitsscopes in Abhängigkeiten

::: readyapi.security.SecurityScopes

## OpenID Connect

::: readyapi.security.OpenIdConnect
