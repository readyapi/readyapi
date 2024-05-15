# Security Tools

When you need to declare dependencies with OAuth2 scopes you use `Security()`.

But you still need to define what is the dependable, the callable that you pass as a parameter to `Depends()` or `Security()`.

There are multiple tools that you can use to create those dependables, and they get integrated into OpenAPI so they are shown in the automatic docs UI, they can be used by automatically generated clients and SDKs, etc.

You can import them from `readyapi.security`:

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

## API Key Security Schemes

::: readyapi.security.APIKeyCookie

::: readyapi.security.APIKeyHeader

::: readyapi.security.APIKeyQuery

## HTTP Authentication Schemes

::: readyapi.security.HTTPBasic

::: readyapi.security.HTTPBearer

::: readyapi.security.HTTPDigest

## HTTP Credentials

::: readyapi.security.HTTPAuthorizationCredentials

::: readyapi.security.HTTPBasicCredentials

## OAuth2 Authentication

::: readyapi.security.OAuth2

::: readyapi.security.OAuth2AuthorizationCodeBearer

::: readyapi.security.OAuth2PasswordBearer

## OAuth2 Password Form

::: readyapi.security.OAuth2PasswordRequestForm

::: readyapi.security.OAuth2PasswordRequestFormStrict

## OAuth2 Security Scopes in Dependencies

::: readyapi.security.SecurityScopes

## OpenID Connect

::: readyapi.security.OpenIdConnect
