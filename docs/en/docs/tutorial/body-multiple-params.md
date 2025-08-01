# Body - Multiple Parameters

Now that we have seen how to use `Path` and `Query`, let's see more advanced uses of request body declarations.

## Mix `Path`, `Query` and body parameters

First, of course, you can mix `Path`, `Query` and request body parameter declarations freely and **ReadyAPI** will know what to do.

And you can also declare body parameters as optional, by setting the default to `None`:

{* ../../examples/body_multiple_params/tutorial001_an_py310.py hl[18:20] *}

/// note

Notice that, in this case, the `item` that would be taken from the body is optional. As it has a `None` default value.

///

## Multiple body parameters

In the previous example, the *path operations* would expect a JSON body with the attributes of an `Item`, like:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

But you can also declare multiple body parameters, e.g. `item` and `user`:

{* ../../examples/body_multiple_params/tutorial002_py310.py hl[20] *}


In this case, **ReadyAPI** will notice that there is more than one body parameter in the function (there are two parameters that are Pydantic models).

So, it will then use the parameter names as keys (field names) in the body, and expect a body like:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

/// note

Notice that even though the `item` was declared the same way as before, it is now expected to be inside of the body with a key `item`.

///

**ReadyAPI** will do the automatic conversion from the request, so that the parameter `item` receives its specific content and the same for `user`.

It will perform the validation of the compound data, and will document it like that for the OpenAPI schema and automatic docs.

## Singular values in body

The same way there is a `Query` and `Path` to define extra data for query and path parameters, **ReadyAPI** provides an equivalent `Body`.

For example, extending the previous model, you could decide that you want to have another key `importance` in the same body, besides the `item` and `user`.

If you declare it as is, because it is a singular value, **ReadyAPI** will assume that it is a query parameter.

But you can instruct **ReadyAPI** to treat it as another body key using `Body`:

{* ../../examples/body_multiple_params/tutorial003_an_py310.py hl[23] *}


In this case, **ReadyAPI** will expect a body like:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

Again, it will convert the data types, validate, document, etc.

## Multiple body params and query

Of course, you can also declare additional query parameters whenever you need, additional to any body parameters.

As, by default, singular values are interpreted as query parameters, you don't have to explicitly add a `Query`, you can just do:

```Python
q: Union[str, None] = None
```

Or in Python 3.10 and above:

```Python
q: str | None = None
```

For example:

{* ../../examples/body_multiple_params/tutorial004_an_py310.py hl[28] *}


/// info

`Body` also has all the same extra validation and metadata parameters as `Query`,`Path` and others you will see later.

///

## Embed a single body parameter

Let's say you only have a single `item` body parameter from a Pydantic model `Item`.

By default, **ReadyAPI** will then expect its body directly.

But if you want it to expect a JSON with a key `item` and inside of it the model contents, as it does when you declare extra body parameters, you can use the special `Body` parameter `embed`:

```Python
item: Item = Body(embed=True)
```

as in:

{* ../../examples/body_multiple_params/tutorial005_an_py310.py hl[17] *}


In this case **ReadyAPI** will expect a body like:

```JSON hl_lines="2"
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

instead of:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

## Recap

You can add multiple body parameters to your *path operation function*, even though a request can only have a single body.

But **ReadyAPI** will handle it, give you the correct data in your function, and validate and document the correct schema in the *path operation*.

You can also declare singular values to be received as part of the body.

And you can instruct **ReadyAPI** to embed the body in a key even when there is only a single parameter declared.
