# 📨 🏷 - 📨 🆎

👆 💪 📣 🆎 ⚙️ 📨 ✍ *➡ 🛠️ 🔢* **📨 🆎**.

👆 💪 ⚙️ **🆎 ✍** 🎏 🌌 👆 🔜 🔢 💽 🔢 **🔢**, 👆 💪 ⚙️ Pydantic 🏷, 📇, 📖, 📊 💲 💖 🔢, 🎻, ♒️.

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="18  23"
{!> ../../docs_src/response_model/tutorial001_01.py!}
```

////

//// tab | 🐍 3️⃣.9️⃣ &amp; 🔛

```Python hl_lines="18  23"
{!> ../../docs_src/response_model/tutorial001_01_py39.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="16  21"
{!> ../../docs_src/response_model/tutorial001_01_py310.py!}
```

////

ReadyAPI 🔜 ⚙️ 👉 📨 🆎:

* **✔** 📨 💽.
    * 🚥 💽 ❌ (✅ 👆 ❌ 🏑), ⚫️ ⛓ 👈 *👆* 📱 📟 💔, 🚫 🛬 ⚫️❔ ⚫️ 🔜, &amp; ⚫️ 🔜 📨 💽 ❌ ↩️ 🛬 ❌ 💽. 👉 🌌 👆 &amp; 👆 👩‍💻 💪 🎯 👈 👫 🔜 📨 💽 &amp; 💽 💠 📈.
* 🚮 **🎻 🔗** 📨, 🗄 *➡ 🛠️*.
    * 👉 🔜 ⚙️ **🏧 🩺**.
    * ⚫️ 🔜 ⚙️ 🏧 👩‍💻 📟 ⚡ 🧰.

✋️ 🏆 🥈:

* ⚫️ 🔜 **📉 &amp; ⛽** 🔢 📊 ⚫️❔ 🔬 📨 🆎.
    * 👉 ✴️ ⚠ **💂‍♂**, 👥 🔜 👀 🌅 👈 🔛.

## `response_model` 🔢

📤 💼 🌐❔ 👆 💪 ⚖️ 💚 📨 💽 👈 🚫 ⚫️❔ ⚫️❔ 🆎 📣.

🖼, 👆 💪 💚 **📨 📖** ⚖️ 💽 🎚, ✋️ **📣 ⚫️ Pydantic 🏷**. 👉 🌌 Pydantic 🏷 🔜 🌐 💽 🧾, 🔬, ♒️. 🎚 👈 👆 📨 (✅ 📖 ⚖️ 💽 🎚).

🚥 👆 🚮 📨 🆎 ✍, 🧰 &amp; 👨‍🎨 🔜 😭 ⏮️ (☑) ❌ 💬 👆 👈 👆 🔢 🛬 🆎 (✅#️⃣) 👈 🎏 ⚪️➡️ ⚫️❔ 👆 📣 (✅ Pydantic 🏷).

📚 💼, 👆 💪 ⚙️ *➡ 🛠️ 👨‍🎨* 🔢 `response_model` ↩️ 📨 🆎.

👆 💪 ⚙️ `response_model` 🔢 🙆 *➡ 🛠️*:

* `@app.get()`
* `@app.post()`
* `@app.put()`
* `@app.delete()`
* ♒️.

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="17  22  24-27"
{!> ../../docs_src/response_model/tutorial001.py!}
```

////

//// tab | 🐍 3️⃣.9️⃣ &amp; 🔛

```Python hl_lines="17  22  24-27"
{!> ../../docs_src/response_model/tutorial001_py39.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="17  22  24-27"
{!> ../../docs_src/response_model/tutorial001_py310.py!}
```

////

/// note

👀 👈 `response_model` 🔢 "👨‍🎨" 👩‍🔬 (`get`, `post`, ♒️). 🚫 👆 *➡ 🛠️ 🔢*, 💖 🌐 🔢 &amp; 💪.

///

`response_model` 📨 🎏 🆎 👆 🔜 📣 Pydantic 🏷 🏑,, ⚫️ 💪 Pydantic 🏷, ✋️ ⚫️ 💪, ✅ `list` Pydantic 🏷, 💖 `List[Item]`.

ReadyAPI 🔜 ⚙️ 👉 `response_model` 🌐 💽 🧾, 🔬, ♒️. &amp; **🗜 &amp; ⛽ 🔢 📊** 🚮 🆎 📄.

/// tip

🚥 👆 ✔️ ⚠ 🆎 ✅ 👆 👨‍🎨, ✍, ♒️, 👆 💪 📣 🔢 📨 🆎 `Any`.

👈 🌌 👆 💬 👨‍🎨 👈 👆 😫 🛬 🕳. ✋️ ReadyAPI 🔜 💽 🧾, 🔬, 🖥, ♒️. ⏮️ `response_model`.

///

### `response_model` 📫

🚥 👆 📣 👯‍♂️ 📨 🆎 &amp; `response_model`, `response_model` 🔜 ✊ 📫 &amp; ⚙️ ReadyAPI.

👉 🌌 👆 💪 🚮 ☑ 🆎 ✍ 👆 🔢 🕐❔ 👆 🛬 🆎 🎏 🌘 📨 🏷, ⚙️ 👨‍🎨 &amp; 🧰 💖 ✍. &amp; 👆 💪 ✔️ ReadyAPI 💽 🔬, 🧾, ♒️. ⚙️ `response_model`.

👆 💪 ⚙️ `response_model=None` ❎ 🏗 📨 🏷 👈 *➡ 🛠️*, 👆 5️⃣📆 💪 ⚫️ 🚥 👆 ❎ 🆎 ✍ 👜 👈 🚫 ☑ Pydantic 🏑, 👆 🔜 👀 🖼 👈 1️⃣ 📄 🔛.

## 📨 🎏 🔢 💽

📥 👥 📣 `UserIn` 🏷, ⚫️ 🔜 🔌 🔢 🔐:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="9  11"
{!> ../../docs_src/response_model/tutorial002.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="7  9"
{!> ../../docs_src/response_model/tutorial002_py310.py!}
```

////

/// info

⚙️ `EmailStr`, 🥇 ❎ <a href="https://github.com/JoshData/python-email-validator" class="external-link" target="_blank">`email-validator`</a>.

🤶 Ⓜ. `pip install email-validator`
⚖️ `pip install pydantic[email]`.

///

&amp; 👥 ⚙️ 👉 🏷 📣 👆 🔢 &amp; 🎏 🏷 📣 👆 🔢:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="18"
{!> ../../docs_src/response_model/tutorial002.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="16"
{!> ../../docs_src/response_model/tutorial002_py310.py!}
```

////

🔜, 🕐❔ 🖥 🏗 👩‍💻 ⏮️ 🔐, 🛠️ 🔜 📨 🎏 🔐 📨.

👉 💼, ⚫️ 💪 🚫 ⚠, ↩️ ⚫️ 🎏 👩‍💻 📨 🔐.

✋️ 🚥 👥 ⚙️ 🎏 🏷 ➕1️⃣ *➡ 🛠️*, 👥 💪 📨 👆 👩‍💻 🔐 🔠 👩‍💻.

/// danger

🙅 🏪 ✅ 🔐 👩‍💻 ⚖️ 📨 ⚫️ 📨 💖 👉, 🚥 👆 💭 🌐 ⚠ &amp; 👆 💭 ⚫️❔ 👆 🔨.

///

## 🚮 🔢 🏷

👥 💪 ↩️ ✍ 🔢 🏷 ⏮️ 🔢 🔐 &amp; 🔢 🏷 🍵 ⚫️:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="9  11  16"
{!> ../../docs_src/response_model/tutorial003.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="9  11  16"
{!> ../../docs_src/response_model/tutorial003_py310.py!}
```

////

📥, ✋️ 👆 *➡ 🛠️ 🔢* 🛬 🎏 🔢 👩‍💻 👈 🔌 🔐:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="24"
{!> ../../docs_src/response_model/tutorial003.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="24"
{!> ../../docs_src/response_model/tutorial003_py310.py!}
```

////

...👥 📣 `response_model` 👆 🏷 `UserOut`, 👈 🚫 🔌 🔐:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="22"
{!> ../../docs_src/response_model/tutorial003.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="22"
{!> ../../docs_src/response_model/tutorial003_py310.py!}
```

////

, **ReadyAPI** 🔜 ✊ 💅 🖥 👅 🌐 💽 👈 🚫 📣 🔢 🏷 (⚙️ Pydantic).

### `response_model` ⚖️ 📨 🆎

👉 💼, ↩️ 2️⃣ 🏷 🎏, 🚥 👥 ✍ 🔢 📨 🆎 `UserOut`, 👨‍🎨 &amp; 🧰 🔜 😭 👈 👥 🛬 ❌ 🆎, 📚 🎏 🎓.

👈 ⚫️❔ 👉 🖼 👥 ✔️ 📣 ⚫️ `response_model` 🔢.

...✋️ 😣 👂 🔛 👀 ❔ ❎ 👈.

## 📨 🆎 &amp; 💽 🖥

➡️ 😣 ⚪️➡️ ⏮️ 🖼. 👥 💚 **✍ 🔢 ⏮️ 1️⃣ 🆎** ✋️ 📨 🕳 👈 🔌 **🌅 💽**.

👥 💚 ReadyAPI 🚧 **🖥** 📊 ⚙️ 📨 🏷.

⏮️ 🖼, ↩️ 🎓 🎏, 👥 ✔️ ⚙️ `response_model` 🔢. ✋️ 👈 ⛓ 👈 👥 🚫 🤚 🐕‍🦺 ⚪️➡️ 👨‍🎨 &amp; 🧰 ✅ 🔢 📨 🆎.

✋️ 🌅 💼 🌐❔ 👥 💪 🕳 💖 👉, 👥 💚 🏷 **⛽/❎** 📊 👉 🖼.

&amp; 👈 💼, 👥 💪 ⚙️ 🎓 &amp; 🧬 ✊ 📈 🔢 **🆎 ✍** 🤚 👍 🐕‍🦺 👨‍🎨 &amp; 🧰, &amp; 🤚 ReadyAPI **💽 🖥**.

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="9-13  15-16  20"
{!> ../../docs_src/response_model/tutorial003_01.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="7-10  13-14  18"
{!> ../../docs_src/response_model/tutorial003_01_py310.py!}
```

////

⏮️ 👉, 👥 🤚 🏭 🐕‍🦺, ⚪️➡️ 👨‍🎨 &amp; ✍ 👉 📟 ☑ ⚖ 🆎, ✋️ 👥 🤚 💽 🖥 ⚪️➡️ ReadyAPI.

❔ 🔨 👉 👷 ❓ ➡️ ✅ 👈 👅. 👶

### 🆎 ✍ &amp; 🏭

🥇 ➡️ 👀 ❔ 👨‍🎨, ✍ &amp; 🎏 🧰 🔜 👀 👉.

`BaseUser` ✔️ 🧢 🏑. ⤴️ `UserIn` 😖 ⚪️➡️ `BaseUser` &amp; 🚮 `password` 🏑,, ⚫️ 🔜 🔌 🌐 🏑 ⚪️➡️ 👯‍♂️ 🏷.

👥 ✍ 🔢 📨 🆎 `BaseUser`, ✋️ 👥 🤙 🛬 `UserIn` 👐.

👨‍🎨, ✍, &amp; 🎏 🧰 🏆 🚫 😭 🔃 👉 ↩️, ⌨ ⚖, `UserIn` 🏿 `BaseUser`, ❔ ⛓ ⚫️ *☑* 🆎 🕐❔ ⚫️❔ ⌛ 🕳 👈 `BaseUser`.

### ReadyAPI 💽 🖥

🔜, ReadyAPI, ⚫️ 🔜 👀 📨 🆎 &amp; ⚒ 💭 👈 ⚫️❔ 👆 📨 🔌 **🕴** 🏑 👈 📣 🆎.

ReadyAPI 🔨 📚 👜 🔘 ⏮️ Pydantic ⚒ 💭 👈 📚 🎏 🚫 🎓 🧬 🚫 ⚙️ 📨 💽 🖥, ⏪ 👆 💪 🔚 🆙 🛬 🌅 🌅 💽 🌘 ⚫️❔ 👆 📈.

👉 🌌, 👆 💪 🤚 🏆 👯‍♂️ 🌏: 🆎 ✍ ⏮️ **🏭 🐕‍🦺** &amp; **💽 🖥**.

## 👀 ⚫️ 🩺

🕐❔ 👆 👀 🏧 🩺, 👆 💪 ✅ 👈 🔢 🏷 &amp; 🔢 🏷 🔜 👯‍♂️ ✔️ 👫 👍 🎻 🔗:

<img src="/img/tutorial/response-model/image01.png">

&amp; 👯‍♂️ 🏷 🔜 ⚙️ 🎓 🛠️ 🧾:

<img src="/img/tutorial/response-model/image02.png">

## 🎏 📨 🆎 ✍

📤 5️⃣📆 💼 🌐❔ 👆 📨 🕳 👈 🚫 ☑ Pydantic 🏑 &amp; 👆 ✍ ⚫️ 🔢, 🕴 🤚 🐕‍🦺 🚚 🏭 (👨‍🎨, ✍, ♒️).

### 📨 📨 🔗

🏆 ⚠ 💼 🔜 [🛬 📨 🔗 🔬 ⏪ 🏧 🩺](../advanced/response-directly.md){.internal-link target=_blank}.

```Python hl_lines="8  10-11"
{!> ../../docs_src/response_model/tutorial003_02.py!}
```

👉 🙅 💼 🍵 🔁 ReadyAPI ↩️ 📨 🆎 ✍ 🎓 (⚖️ 🏿) `Response`.

&amp; 🧰 🔜 😄 ↩️ 👯‍♂️ `RedirectResponse` &amp; `JSONResponse` 🏿 `Response`, 🆎 ✍ ☑.

### ✍ 📨 🏿

👆 💪 ⚙️ 🏿 `Response` 🆎 ✍:

```Python hl_lines="8-9"
{!> ../../docs_src/response_model/tutorial003_03.py!}
```

👉 🔜 👷 ↩️ `RedirectResponse` 🏿 `Response`, &amp; ReadyAPI 🔜 🔁 🍵 👉 🙅 💼.

### ❌ 📨 🆎 ✍

✋️ 🕐❔ 👆 📨 🎏 ❌ 🎚 👈 🚫 ☑ Pydantic 🆎 (✅ 💽 🎚) &amp; 👆 ✍ ⚫️ 💖 👈 🔢, ReadyAPI 🔜 🔄 ✍ Pydantic 📨 🏷 ⚪️➡️ 👈 🆎 ✍, &amp; 🔜 ❌.

🎏 🔜 🔨 🚥 👆 ✔️ 🕳 💖 <abbr title='A union between multiple types means "any of these types".'>🇪🇺</abbr> 🖖 🎏 🆎 🌐❔ 1️⃣ ⚖️ 🌅 👫 🚫 ☑ Pydantic 🆎, 🖼 👉 🔜 ❌ 👶:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="10"
{!> ../../docs_src/response_model/tutorial003_04.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="8"
{!> ../../docs_src/response_model/tutorial003_04_py310.py!}
```

////

...👉 ❌ ↩️ 🆎 ✍ 🚫 Pydantic 🆎 &amp; 🚫 👁 `Response` 🎓 ⚖️ 🏿, ⚫️ 🇪🇺 (🙆 2️⃣) 🖖 `Response` &amp; `dict`.

### ❎ 📨 🏷

▶️ ⚪️➡️ 🖼 🔛, 👆 5️⃣📆 🚫 💚 ✔️ 🔢 💽 🔬, 🧾, 🖥, ♒️. 👈 🎭 ReadyAPI.

✋️ 👆 💪 💚 🚧 📨 🆎 ✍ 🔢 🤚 🐕‍🦺 ⚪️➡️ 🧰 💖 👨‍🎨 &amp; 🆎 ☑ (✅ ✍).

👉 💼, 👆 💪 ❎ 📨 🏷 ⚡ ⚒ `response_model=None`:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="9"
{!> ../../docs_src/response_model/tutorial003_05.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="7"
{!> ../../docs_src/response_model/tutorial003_05_py310.py!}
```

////

👉 🔜 ⚒ ReadyAPI 🚶 📨 🏷 ⚡ &amp; 👈 🌌 👆 💪 ✔️ 🙆 📨 🆎 ✍ 👆 💪 🍵 ⚫️ 🤕 👆 ReadyAPI 🈸. 👶

## 📨 🏷 🔢 🔢

👆 📨 🏷 💪 ✔️ 🔢 💲, 💖:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="11  13-14"
{!> ../../docs_src/response_model/tutorial004.py!}
```

////

//// tab | 🐍 3️⃣.9️⃣ &amp; 🔛

```Python hl_lines="11  13-14"
{!> ../../docs_src/response_model/tutorial004_py39.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="9  11-12"
{!> ../../docs_src/response_model/tutorial004_py310.py!}
```

////

* `description: Union[str, None] = None` (⚖️ `str | None = None` 🐍 3️⃣.1️⃣0️⃣) ✔️ 🔢 `None`.
* `tax: float = 10.5` ✔️ 🔢 `10.5`.
* `tags: List[str] = []` 🔢 🛁 📇: `[]`.

✋️ 👆 💪 💚 🚫 👫 ⚪️➡️ 🏁 🚥 👫 🚫 🤙 🏪.

🖼, 🚥 👆 ✔️ 🏷 ⏮️ 📚 📦 🔢 ☁ 💽, ✋️ 👆 🚫 💚 📨 📶 📏 🎻 📨 🌕 🔢 💲.

### ⚙️ `response_model_exclude_unset` 🔢

👆 💪 ⚒ *➡ 🛠️ 👨‍🎨* 🔢 `response_model_exclude_unset=True`:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="24"
{!> ../../docs_src/response_model/tutorial004.py!}
```

////

//// tab | 🐍 3️⃣.9️⃣ &amp; 🔛

```Python hl_lines="24"
{!> ../../docs_src/response_model/tutorial004_py39.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="22"
{!> ../../docs_src/response_model/tutorial004_py310.py!}
```

////

&amp; 👈 🔢 💲 🏆 🚫 🔌 📨, 🕴 💲 🤙 ⚒.

, 🚥 👆 📨 📨 👈 *➡ 🛠️* 🏬 ⏮️ 🆔 `foo`, 📨 (🚫 ✅ 🔢 💲) 🔜:

```JSON
{
    "name": "Foo",
    "price": 50.2
}
```

/// info

ReadyAPI ⚙️ Pydantic 🏷 `.dict()` ⏮️ <a href="https://docs.pydantic.dev/latest/concepts/serialization/#modeldict" class="external-link" target="_blank">🚮 `exclude_unset` 🔢</a> 🏆 👉.

///

/// info

👆 💪 ⚙️:

* `response_model_exclude_defaults=True`
* `response_model_exclude_none=True`

🔬 <a href="https://docs.pydantic.dev/latest/concepts/serialization/#modeldict" class="external-link" target="_blank">Pydantic 🩺</a> `exclude_defaults` &amp; `exclude_none`.

///

#### 📊 ⏮️ 💲 🏑 ⏮️ 🔢

✋️ 🚥 👆 📊 ✔️ 💲 🏷 🏑 ⏮️ 🔢 💲, 💖 🏬 ⏮️ 🆔 `bar`:

```Python hl_lines="3  5"
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
```

👫 🔜 🔌 📨.

#### 📊 ⏮️ 🎏 💲 🔢

🚥 📊 ✔️ 🎏 💲 🔢 🕐, 💖 🏬 ⏮️ 🆔 `baz`:

```Python hl_lines="3  5-6"
{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

ReadyAPI 🙃 🥃 (🤙, Pydantic 🙃 🥃) 🤔 👈, ✋️ `description`, `tax`, &amp; `tags` ✔️ 🎏 💲 🔢, 👫 ⚒ 🎯 (↩️ ✊ ⚪️➡️ 🔢).

, 👫 🔜 🔌 🎻 📨.

/// tip

👀 👈 🔢 💲 💪 🕳, 🚫 🕴 `None`.

👫 💪 📇 (`[]`), `float` `10.5`, ♒️.

///

### `response_model_include` &amp; `response_model_exclude`

👆 💪 ⚙️ *➡ 🛠️ 👨‍🎨* 🔢 `response_model_include` &amp; `response_model_exclude`.

👫 ✊ `set` `str` ⏮️ 📛 🔢 🔌 (❎ 🎂) ⚖️ 🚫 (✅ 🎂).

👉 💪 ⚙️ ⏩ ⌨ 🚥 👆 ✔️ 🕴 1️⃣ Pydantic 🏷 &amp; 💚 ❎ 💽 ⚪️➡️ 🔢.

/// tip

✋️ ⚫️ 👍 ⚙️ 💭 🔛, ⚙️ 💗 🎓, ↩️ 👫 🔢.

👉 ↩️ 🎻 🔗 🏗 👆 📱 🗄 (&amp; 🩺) 🔜 1️⃣ 🏁 🏷, 🚥 👆 ⚙️ `response_model_include` ⚖️ `response_model_exclude` 🚫 🔢.

👉 ✔ `response_model_by_alias` 👈 👷 ➡.

///

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="31  37"
{!> ../../docs_src/response_model/tutorial005.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="29  35"
{!> ../../docs_src/response_model/tutorial005_py310.py!}
```

////

/// tip

❕ `{"name", "description"}` ✍ `set` ⏮️ 📚 2️⃣ 💲.

⚫️ 🌓 `set(["name", "description"])`.

///

#### ⚙️ `list`Ⓜ ↩️ `set`Ⓜ

🚥 👆 💭 ⚙️ `set` &amp; ⚙️ `list` ⚖️ `tuple` ↩️, ReadyAPI 🔜 🗜 ⚫️ `set` &amp; ⚫️ 🔜 👷 ☑:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="31  37"
{!> ../../docs_src/response_model/tutorial006.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="29  35"
{!> ../../docs_src/response_model/tutorial006_py310.py!}
```

////

## 🌃

⚙️ *➡ 🛠️ 👨‍🎨* 🔢 `response_model` 🔬 📨 🏷 &amp; ✴️ 🚚 📢 💽 ⛽ 👅.

⚙️ `response_model_exclude_unset` 📨 🕴 💲 🎯 ⚒.
