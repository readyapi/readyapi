# Dependencies - `Depends()` and `Security()`

## `Depends()`

Dependencies are handled mainly with the special function `Depends()` that takes a callable.

Here is the reference for it and its parameters.

You can import it directly from `readyapi`:

```python
from readyapi import Depends
```

::: readyapi.Depends

## `Security()`

For many scenarios, you can handle security (authorization, authentication, etc.) with dependencies, using `Depends()`.

But when you want to also declare OAuth2 scopes, you can use `Security()` instead of `Depends()`.

You can import `Security()` directly from `readyapi`:

```python
from readyapi import Security
```

::: readyapi.Security
