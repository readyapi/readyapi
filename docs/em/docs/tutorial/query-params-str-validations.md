# 🔢 🔢 &amp; 🎻 🔬

**ReadyAPI** ✔ 👆 📣 🌖 ℹ &amp; 🔬 👆 🔢.

➡️ ✊ 👉 🈸 🖼:

{* ../../examples/query_params_str_validations/tutorial001.py hl[9] *}

🔢 🔢 `q` 🆎 `Union[str, None]` (⚖️ `str | None` 🐍 3️⃣.1️⃣0️⃣), 👈 ⛓ 👈 ⚫️ 🆎 `str` ✋️ 💪 `None`, &amp; 👐, 🔢 💲 `None`, ReadyAPI 🔜 💭 ⚫️ 🚫 ✔.

/// note

ReadyAPI 🔜 💭 👈 💲 `q` 🚫 ✔ ↩️ 🔢 💲 `= None`.

 `Union` `Union[str, None]` 🔜 ✔ 👆 👨‍🎨 🤝 👆 👍 🐕‍🦺 &amp; 🔍 ❌.

///

## 🌖 🔬

👥 🔜 🛠️ 👈 ✋️ `q` 📦, 🕐❔ ⚫️ 🚚, **🚮 📐 🚫 📉 5️⃣0️⃣ 🦹**.

### 🗄 `Query`

🏆 👈, 🥇 🗄 `Query` ⚪️➡️ `readyapi`:

{* ../../examples/query_params_str_validations/tutorial002.py hl[3] *}

## ⚙️ `Query` 🔢 💲

&amp; 🔜 ⚙️ ⚫️ 🔢 💲 👆 🔢, ⚒ 🔢 `max_length` 5️⃣0️⃣:

{* ../../examples/query_params_str_validations/tutorial002.py hl[9] *}

👥 ✔️ ❎ 🔢 💲 `None` 🔢 ⏮️ `Query()`, 👥 💪 🔜 ⚒ 🔢 💲 ⏮️ 🔢 `Query(default=None)`, ⚫️ 🍦 🎏 🎯 ⚖ 👈 🔢 💲.

:

```Python
q: Union[str, None] = Query(default=None)
```

...⚒ 🔢 📦, 🎏:

```Python
q: Union[str, None] = None
```

&amp; 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛:

```Python
q: str | None = Query(default=None)
```

...⚒ 🔢 📦, 🎏:

```Python
q: str | None = None
```

✋️ ⚫️ 📣 ⚫️ 🎯 💆‍♂ 🔢 🔢.

/// info

✔️ 🤯 👈 🌅 ⚠ 🍕 ⚒ 🔢 📦 🍕:

```Python
= None
```

⚖️:

```Python
= Query(default=None)
```

⚫️ 🔜 ⚙️ 👈 `None` 🔢 💲, &amp; 👈 🌌 ⚒ 🔢 **🚫 ✔**.

 `Union[str, None]` 🍕 ✔ 👆 👨‍🎨 🚚 👻 🐕‍🦺, ✋️ ⚫️ 🚫 ⚫️❔ 💬 ReadyAPI 👈 👉 🔢 🚫 ✔.

///

⤴️, 👥 💪 🚶‍♀️ 🌅 🔢 `Query`. 👉 💼, `max_length` 🔢 👈 ✔ 🎻:

```Python
q: Union[str, None] = Query(default=None, max_length=50)
```

👉 🔜 ✔ 📊, 🎦 🆑 ❌ 🕐❔ 📊 🚫 ☑, &amp; 📄 🔢 🗄 🔗 *➡ 🛠️*.

## 🚮 🌅 🔬

👆 💪 🚮 🔢 `min_length`:

{* ../../examples/query_params_str_validations/tutorial003.py hl[10] *}

## 🚮 🥔 🧬

👆 💪 🔬 <abbr title="A regular expression, regex or regexp is a sequence of characters that define a search pattern for strings.">🥔 🧬</abbr> 👈 🔢 🔜 🏏:

{* ../../examples/query_params_str_validations/tutorial004.py hl[11] *}

👉 🎯 🥔 🧬 ✅ 👈 📨 🔢 💲:

* `^`: ▶️ ⏮️ 📄 🦹, 🚫 ✔️ 🦹 ⏭.
* `fixedquery`: ✔️ ☑ 💲 `fixedquery`.
* `$`: 🔚 📤, 🚫 ✔️ 🙆 🌖 🦹 ⏮️ `fixedquery`.

🚥 👆 💭 💸 ⏮️ 🌐 👉 **"🥔 🧬"** 💭, 🚫 😟. 👫 🏋️ ❔ 📚 👫👫. 👆 💪 📚 💩 🍵 💆‍♂ 🥔 🧬.

✋️ 🕐❔ 👆 💪 👫 &amp; 🚶 &amp; 💡 👫, 💭 👈 👆 💪 ⏪ ⚙️ 👫 🔗 **ReadyAPI**.

## 🔢 💲

🎏 🌌 👈 👆 💪 🚶‍♀️ `None` 💲 `default` 🔢, 👆 💪 🚶‍♀️ 🎏 💲.

➡️ 💬 👈 👆 💚 📣 `q` 🔢 🔢 ✔️ `min_length` `3`, &amp; ✔️ 🔢 💲 `"fixedquery"`:

{* ../../examples/query_params_str_validations/tutorial005.py hl[7] *}

/// note

✔️ 🔢 💲 ⚒ 🔢 📦.

///

## ⚒ ⚫️ ✔

🕐❔ 👥 🚫 💪 📣 🌅 🔬 ⚖️ 🗃, 👥 💪 ⚒ `q` 🔢 🔢 ✔ 🚫 📣 🔢 💲, 💖:

```Python
q: str
```

↩️:

```Python
q: Union[str, None] = None
```

✋️ 👥 🔜 📣 ⚫️ ⏮️ `Query`, 🖼 💖:

```Python
q: Union[str, None] = Query(default=None, min_length=3)
```

, 🕐❔ 👆 💪 📣 💲 ✔ ⏪ ⚙️ `Query`, 👆 💪 🎯 🚫 📣 🔢 💲:

{* ../../examples/query_params_str_validations/tutorial006.py hl[7] *}

### ✔ ⏮️ `None`

👆 💪 📣 👈 🔢 💪 🚫 `None`, ✋️ 👈 ⚫️ ✔. 👉 🔜 ⚡ 👩‍💻 📨 💲, 🚥 💲 `None`.

👈, 👆 💪 📣 👈 `None` ☑ 🆎 ✋️ ⚙️ `default=...`:

{* ../../examples/query_params_str_validations/tutorial006c.py hl[9] *}

/// tip

Pydantic, ❔ ⚫️❔ 🏋️ 🌐 💽 🔬 &amp; 🛠️ ReadyAPI, ✔️ 🎁 🎭 🕐❔ 👆 ⚙️ `Optional` ⚖️ `Union[Something, None]` 🍵 🔢 💲, 👆 💪 ✍ 🌅 🔃 ⚫️ Pydantic 🩺 🔃 <a href="https://docs.pydantic.dev/latest/concepts/models/#required-optional-fields" class="external-link" target="_blank">✔ 📦 🏑</a>.

///

## 🔢 🔢 📇 / 💗 💲

🕐❔ 👆 🔬 🔢 🔢 🎯 ⏮️ `Query` 👆 💪 📣 ⚫️ 📨 📇 💲, ⚖️ 🙆‍♀ 🎏 🌌, 📨 💗 💲.

🖼, 📣 🔢 🔢 `q` 👈 💪 😑 💗 🕰 📛, 👆 💪 ✍:

{* ../../examples/query_params_str_validations/tutorial011.py hl[9] *}

⤴️, ⏮️ 📛 💖:

```
http://localhost:8000/items/?q=foo&q=bar
```

👆 🔜 📨 💗 `q` *🔢 🔢'* 💲 (`foo` &amp; `bar`) 🐍 `list` 🔘 👆 *➡ 🛠️ 🔢*, *🔢 🔢* `q`.

, 📨 👈 📛 🔜:

```JSON
{
  "q": [
    "foo",
    "bar"
  ]
}
```

/// tip

📣 🔢 🔢 ⏮️ 🆎 `list`, 💖 🖼 🔛, 👆 💪 🎯 ⚙️ `Query`, ⏪ ⚫️ 🔜 🔬 📨 💪.

///

🎓 🛠️ 🩺 🔜 ℹ ➡️, ✔ 💗 💲:

<img src="/img/tutorial/query-params-str-validations/image02.png">

### 🔢 🔢 📇 / 💗 💲 ⏮️ 🔢

&amp; 👆 💪 🔬 🔢 `list` 💲 🚥 👌 🚚:

{* ../../examples/query_params_str_validations/tutorial012.py hl[9] *}

🚥 👆 🚶:

```
http://localhost:8000/items/
```

🔢 `q` 🔜: `["foo", "bar"]` &amp; 👆 📨 🔜:

```JSON
{
  "q": [
    "foo",
    "bar"
  ]
}
```

#### ⚙️ `list`

👆 💪 ⚙️ `list` 🔗 ↩️ `List[str]` (⚖️ `list[str]` 🐍 3️⃣.9️⃣ ➕):

{* ../../examples/query_params_str_validations/tutorial013.py hl[7] *}

/// note

✔️ 🤯 👈 👉 💼, ReadyAPI 🏆 🚫 ✅ 🎚 📇.

🖼, `List[int]` 🔜 ✅ (&amp; 📄) 👈 🎚 📇 🔢. ✋️ `list` 😞 🚫🔜.

///

## 📣 🌅 🗃

👆 💪 🚮 🌅 ℹ 🔃 🔢.

👈 ℹ 🔜 🔌 🏗 🗄 &amp; ⚙️ 🧾 👩‍💻 🔢 &amp; 🔢 🧰.

/// note

✔️ 🤯 👈 🎏 🧰 5️⃣📆 ✔️ 🎏 🎚 🗄 🐕‍🦺.

👫 💪 🚫 🎦 🌐 ➕ ℹ 📣, 👐 🌅 💼, ❌ ⚒ ⏪ 📄 🛠️.

///

👆 💪 🚮 `title`:

{* ../../examples/query_params_str_validations/tutorial007.py hl[10] *}

&amp; `description`:

{* ../../examples/query_params_str_validations/tutorial008.py hl[13] *}

## 📛 🔢

🌈 👈 👆 💚 🔢 `item-query`.

💖:

```
http://127.0.0.1:8000/items/?item-query=foobaritems
```

✋️ `item-query` 🚫 ☑ 🐍 🔢 📛.

🔐 🔜 `item_query`.

✋️ 👆 💪 ⚫️ ⚫️❔ `item-query`...

⤴️ 👆 💪 📣 `alias`, &amp; 👈 📛 ⚫️❔ 🔜 ⚙️ 🔎 🔢 💲:

{* ../../examples/query_params_str_validations/tutorial009.py hl[9] *}

## 😛 🔢

🔜 ➡️ 💬 👆 🚫 💖 👉 🔢 🚫🔜.

👆 ✔️ 👈 ⚫️ 📤 ⏪ ↩️ 📤 👩‍💻 ⚙️ ⚫️, ✋️ 👆 💚 🩺 🎯 🎦 ⚫️ <abbr title="obsolete, recommended not to use it">😢</abbr>.

⤴️ 🚶‍♀️ 🔢 `deprecated=True` `Query`:

{* ../../examples/query_params_str_validations/tutorial010.py hl[18] *}

🩺 🔜 🎦 ⚫️ 💖 👉:

<img src="/img/tutorial/query-params-str-validations/image01.png">

## 🚫 ⚪️➡️ 🗄

🚫 🔢 🔢 ⚪️➡️ 🏗 🗄 🔗 (&amp; ➡️, ⚪️➡️ 🏧 🧾 ⚙️), ⚒ 🔢 `include_in_schema` `Query` `False`:

{* ../../examples/query_params_str_validations/tutorial014.py hl[10] *}

## 🌃

👆 💪 📣 🌖 🔬 &amp; 🗃 👆 🔢.

💊 🔬 &amp; 🗃:

* `alias`
* `title`
* `description`
* `deprecated`

🔬 🎯 🎻:

* `min_length`
* `max_length`
* `regex`

👫 🖼 👆 👀 ❔ 📣 🔬 `str` 💲.

👀 ⏭ 📃 👀 ❔ 📣 🔬 🎏 🆎, 💖 🔢.
