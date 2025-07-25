# Settings and Environment Variables

In many cases your application could need some external settings or configurations, for example secret keys, database credentials, credentials for email services, etc.

Most of these settings are variable (can change), like database URLs. And many could be sensitive, like secrets.

For this reason it's common to provide them in environment variables that are read by the application.

/// tip

To understand environment variables you can read [Environment Variables](../environment-variables.md){.internal-link target=_blank}.

///

## Types and validation

These environment variables can only handle text strings, as they are external to Python and have to be compatible with other programs and the rest of the system (and even with different operating systems, as Linux, Windows, macOS).

That means that any value read in Python from an environment variable will be a `str`, and any conversion to a different type or any validation has to be done in code.

## Pydantic `Settings`

Fortunately, Pydantic provides a great utility to handle these settings coming from environment variables with <a href="https://docs.pydantic.dev/latest/concepts/pydantic_settings/" class="external-link" target="_blank">Pydantic: Settings management</a>.

### Install `pydantic-settings`

First, make sure you create your [virtual environment](../virtual-environments.md){.internal-link target=_blank}, activate it, and then install the `pydantic-settings` package:

<div class="termy">

```console
$ pip install pydantic-settings
---> 100%
```

</div>

It also comes included when you install the `all` extras with:

<div class="termy">

```console
$ pip install "readyapi[all]"
---> 100%
```

</div>

/// info

In Pydantic v1 it came included with the main package. Now it is distributed as this independent package so that you can choose to install it or not if you don't need that functionality.

///

### Create the `Settings` object

Import `BaseSettings` from Pydantic and create a sub-class, very much like with a Pydantic model.

The same way as with Pydantic models, you declare class attributes with type annotations, and possibly default values.

You can use all the same validation features and tools you use for Pydantic models, like different data types and additional validations with `Field()`.

//// tab | Pydantic v2

{* ../../examples/settings/tutorial001.py hl[2,5:8,11] *}

////

//// tab | Pydantic v1

/// info

In Pydantic v1 you would import `BaseSettings` directly from `pydantic` instead of from `pydantic_settings`.

///

{* ../../examples/settings/tutorial001_pv1.py hl[2,5:8,11] *}

////

/// tip

If you want something quick to copy and paste, don't use this example, use the last one below.

///

Then, when you create an instance of that `Settings` class (in this case, in the `settings` object), Pydantic will read the environment variables in a case-insensitive way, so, an upper-case variable `APP_NAME` will still be read for the attribute `app_name`.

Next it will convert and validate the data. So, when you use that `settings` object, you will have data of the types you declared (e.g. `items_per_user` will be an `int`).

### Use the `settings`

Then you can use the new `settings` object in your application:

{* ../../examples/settings/tutorial001.py hl[18:20] *}

### Run the server

Next, you would run the server passing the configurations as environment variables, for example you could set an `ADMIN_EMAIL` and `APP_NAME` with:

<div class="termy">

```console
$ ADMIN_EMAIL="deadpool@example.com" APP_NAME="ChimichangApp" readyapi run main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

/// tip

To set multiple env vars for a single command just separate them with a space, and put them all before the command.

///

And then the `admin_email` setting would be set to `"deadpool@example.com"`.

The `app_name` would be `"ChimichangApp"`.

And the `items_per_user` would keep its default value of `50`.

## Settings in another module

You could put those settings in another module file as you saw in [Bigger Applications - Multiple Files](../tutorial/bigger-applications.md){.internal-link target=_blank}.

For example, you could have a file `config.py` with:

{* ../../examples/settings/app01/config.py *}

And then use it in a file `main.py`:

{* ../../examples/settings/app01/main.py hl[3,11:13] *}

/// tip

You would also need a file `__init__.py` as you saw in [Bigger Applications - Multiple Files](../tutorial/bigger-applications.md){.internal-link target=_blank}.

///

## Settings in a dependency

In some occasions it might be useful to provide the settings from a dependency, instead of having a global object with `settings` that is used everywhere.

This could be especially useful during testing, as it's very easy to override a dependency with your own custom settings.

### The config file

Coming from the previous example, your `config.py` file could look like:

{* ../../examples/settings/app02/config.py hl[10] *}

Notice that now we don't create a default instance `settings = Settings()`.

### The main app file

Now we create a dependency that returns a new `config.Settings()`.

{* ../../examples/settings/app02_an_py39/main.py hl[6,12:13] *}

/// tip

We'll discuss the `@lru_cache` in a bit.

For now you can assume `get_settings()` is a normal function.

///

And then we can require it from the *path operation function* as a dependency and use it anywhere we need it.

{* ../../examples/settings/app02_an_py39/main.py hl[17,19:21] *}

### Settings and testing

Then it would be very easy to provide a different settings object during testing by creating a dependency override for `get_settings`:

{* ../../examples/settings/app02/test_main.py hl[9:10,13,21] *}

In the dependency override we set a new value for the `admin_email` when creating the new `Settings` object, and then we return that new object.

Then we can test that it is used.

## Reading a `.env` file

If you have many settings that possibly change a lot, maybe in different environments, it might be useful to put them on a file and then read them from it as if they were environment variables.

This practice is common enough that it has a name, these environment variables are commonly placed in a file `.env`, and the file is called a "dotenv".

/// tip

A file starting with a dot (`.`) is a hidden file in Unix-like systems, like Linux and macOS.

But a dotenv file doesn't really have to have that exact filename.

///

Pydantic has support for reading from these types of files using an external library. You can read more at <a href="https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support" class="external-link" target="_blank">Pydantic Settings: Dotenv (.env) support</a>.

/// tip

For this to work, you need to `pip install python-dotenv`.

///

### The `.env` file

You could have a `.env` file with:

```bash
ADMIN_EMAIL="deadpool@example.com"
APP_NAME="ChimichangApp"
```

### Read settings from `.env`

And then update your `config.py` with:

//// tab | Pydantic v2

{* ../../examples/settings/app03_an/config.py hl[9] *}

/// tip

The `model_config` attribute is used just for Pydantic configuration. You can read more at <a href="https://docs.pydantic.dev/latest/concepts/config/" class="external-link" target="_blank">Pydantic: Concepts: Configuration</a>.

///

////

//// tab | Pydantic v1

{* ../../examples/settings/app03_an/config_pv1.py hl[9:10] *}

/// tip

The `Config` class is used just for Pydantic configuration. You can read more at <a href="https://docs.pydantic.dev/1.10/usage/model_config/" class="external-link" target="_blank">Pydantic Model Config</a>.

///

////

/// info

In Pydantic version 1 the configuration was done in an internal class `Config`, in Pydantic version 2 it's done in an attribute `model_config`. This attribute takes a `dict`, and to get autocompletion and inline errors you can import and use `SettingsConfigDict` to define that `dict`.

///

Here we define the config `env_file` inside of your Pydantic `Settings` class, and set the value to the filename with the dotenv file we want to use.

### Creating the `Settings` only once with `lru_cache`

Reading a file from disk is normally a costly (slow) operation, so you probably want to do it only once and then reuse the same settings object, instead of reading it for each request.

But every time we do:

```Python
Settings()
```

a new `Settings` object would be created, and at creation it would read the `.env` file again.

If the dependency function was just like:

```Python
def get_settings():
    return Settings()
```

we would create that object for each request, and we would be reading the `.env` file for each request. ⚠️

But as we are using the `@lru_cache` decorator on top, the `Settings` object will be created only once, the first time it's called. ✔️

{* ../../examples/settings/app03_an_py39/main.py hl[1,11] *}

Then for any subsequent call of `get_settings()` in the dependencies for the next requests, instead of executing the internal code of `get_settings()` and creating a new `Settings` object, it will return the same object that was returned on the first call, again and again.

#### `lru_cache` Technical Details

`@lru_cache` modifies the function it decorates to return the same value that was returned the first time, instead of computing it again, executing the code of the function every time.

So, the function below it will be executed once for each combination of arguments. And then the values returned by each of those combinations of arguments will be used again and again whenever the function is called with exactly the same combination of arguments.

For example, if you have a function:

```Python
@lru_cache
def say_hi(name: str, salutation: str = "Ms."):
    return f"Hello {salutation} {name}"
```

your program could execute like this:

```mermaid
sequenceDiagram

participant code as Code
participant function as say_hi()
participant execute as Execute function

    rect rgba(0, 255, 0, .1)
        code ->> function: say_hi(name="Camila")
        function ->> execute: execute function code
        execute ->> code: return the result
    end

    rect rgba(0, 255, 255, .1)
        code ->> function: say_hi(name="Camila")
        function ->> code: return stored result
    end

    rect rgba(0, 255, 0, .1)
        code ->> function: say_hi(name="Rick")
        function ->> execute: execute function code
        execute ->> code: return the result
    end

    rect rgba(0, 255, 0, .1)
        code ->> function: say_hi(name="Rick", salutation="Mr.")
        function ->> execute: execute function code
        execute ->> code: return the result
    end

    rect rgba(0, 255, 255, .1)
        code ->> function: say_hi(name="Rick")
        function ->> code: return stored result
    end

    rect rgba(0, 255, 255, .1)
        code ->> function: say_hi(name="Camila")
        function ->> code: return stored result
    end
```

In the case of our dependency `get_settings()`, the function doesn't even take any arguments, so it always returns the same value.

That way, it behaves almost as if it was just a global variable. But as it uses a dependency function, then we can override it easily for testing.

`@lru_cache` is part of `functools` which is part of Python's standard library, you can read more about it in the <a href="https://docs.python.org/3/library/functools.html#functools.lru_cache" class="external-link" target="_blank">Python docs for `@lru_cache`</a>.

## Recap

You can use Pydantic Settings to handle the settings or configurations for your application, with all the power of Pydantic models.

* By using a dependency you can simplify testing.
* You can use `.env` files with it.
* Using `@lru_cache` lets you avoid reading the dotenv file again and again for each request, while allowing you to override it during testing.
