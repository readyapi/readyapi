# Body - Fields

The same way you can declare additional validation and metadata in _path operation function_ parameters with `Query`, `Path` and `Body`, you can declare validation and metadata inside of Pydantic models using Pydantic's `Field`.

## Import `Field`

First, you have to import it:

//// tab | Python 3.10+

```Python hl_lines="4"
{!> ../../docs_src/body_fields/tutorial001_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="4"
{!> ../../docs_src/body_fields/tutorial001_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="4"
{!> ../../docs_src/body_fields/tutorial001_an.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip

Prefer to use the `Annotated` version if possible.

///

```Python hl_lines="2"
{!> ../../docs_src/body_fields/tutorial001_py310.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Prefer to use the `Annotated` version if possible.

///

```Python hl_lines="4"
{!> ../../docs_src/body_fields/tutorial001.py!}
```

////

/// warning

Notice that `Field` is imported directly from `pydantic`, not from `readyapi` as are all the rest (`Query`, `Path`, `Body`, etc).

///

## Declare model attributes

You can then use `Field` with model attributes:

//// tab | Python 3.10+

```Python hl_lines="11-14"
{!> ../../docs_src/body_fields/tutorial001_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="11-14"
{!> ../../docs_src/body_fields/tutorial001_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="12-15"
{!> ../../docs_src/body_fields/tutorial001_an.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip

Prefer to use the `Annotated` version if possible.

///

```Python hl_lines="9-12"
{!> ../../docs_src/body_fields/tutorial001_py310.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Prefer to use the `Annotated` version if possible.

///

```Python hl_lines="11-14"
{!> ../../docs_src/body_fields/tutorial001.py!}
```

////

`Field` works the same way as `Query`, `Path` and `Body`, it has all the same parameters, etc.

/// note | "Technical Details"

Actually, `Query`, `Path` and others you'll see next create objects of subclasses of a common `Param` class, which is itself a subclass of Pydantic's `FieldInfo` class.

And Pydantic's `Field` returns an instance of `FieldInfo` as well.

`Body` also returns objects of a subclass of `FieldInfo` directly. And there are others you will see later that are subclasses of the `Body` class.

Remember that when you import `Query`, `Path`, and others from `readyapi`, those are actually functions that return special classes.

///

/// tip

Notice how each model's attribute with a type, default value and `Field` has the same structure as a _path operation function's_ parameter, with `Field` instead of `Path`, `Query` and `Body`.

///

## Add extra information

You can declare extra information in `Field`, `Query`, `Body`, etc. And it will be included in the generated JSON Schema.

You will learn more about adding extra information later in the docs, when learning to declare examples.

/// warning

Extra keys passed to `Field` will also be present in the resulting OpenAPI schema for your application.
As these keys may not necessarily be part of the OpenAPI specification, some OpenAPI tools, for example [the OpenAPI validator](https://validator.swagger.io/), may not work with your generated schema.

///

## Recap

You can use Pydantic's `Field` to declare extra validations and metadata for model attributes.

You can also use the extra keyword arguments to pass additional JSON Schema metadata.
