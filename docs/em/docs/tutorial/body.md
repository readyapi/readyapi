# 📨 💪

🕐❔ 👆 💪 📨 📊 ⚪️➡️ 👩‍💻 (➡️ 💬, 🖥) 👆 🛠️, 👆 📨 ⚫️ **📨 💪**.

**📨** 💪 📊 📨 👩‍💻 👆 🛠️. **📨** 💪 💽 👆 🛠️ 📨 👩‍💻.

👆 🛠️ 🌖 🕧 ✔️ 📨 **📨** 💪. ✋️ 👩‍💻 🚫 🎯 💪 📨 **📨** 💪 🌐 🕰.

📣 **📨** 💪, 👆 ⚙️ <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> 🏷 ⏮️ 🌐 👫 🏋️ &amp; 💰.

/// info

📨 💽, 👆 🔜 ⚙️ 1️⃣: `POST` (🌅 ⚠), `PUT`, `DELETE` ⚖️ `PATCH`.

📨 💪 ⏮️ `GET` 📨 ✔️ ⚠ 🎭 🔧, 👐, ⚫️ 🐕‍🦺 ReadyAPI, 🕴 📶 🏗/😕 ⚙️ 💼.

⚫️ 🚫, 🎓 🩺 ⏮️ 🦁 🎚 🏆 🚫 🎦 🧾 💪 🕐❔ ⚙️ `GET`, &amp; 🗳 🖕 💪 🚫 🐕‍🦺 ⚫️.

///

## 🗄 Pydantic `BaseModel`

🥇, 👆 💪 🗄 `BaseModel` ⚪️➡️ `pydantic`:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="4"
{!> ../../docs_src/body/tutorial001.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="2"
{!> ../../docs_src/body/tutorial001_py310.py!}
```

////

## ✍ 👆 💽 🏷

⤴️ 👆 📣 👆 💽 🏷 🎓 👈 😖 ⚪️➡️ `BaseModel`.

⚙️ 🐩 🐍 🆎 🌐 🔢:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="7-11"
{!> ../../docs_src/body/tutorial001.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="5-9"
{!> ../../docs_src/body/tutorial001_py310.py!}
```

////

🎏 🕐❔ 📣 🔢 🔢, 🕐❔ 🏷 🔢 ✔️ 🔢 💲, ⚫️ 🚫 ✔. ⏪, ⚫️ ✔. ⚙️ `None` ⚒ ⚫️ 📦.

🖼, 👉 🏷 🔛 📣 🎻 "`object`" (⚖️ 🐍 `dict`) 💖:

```JSON
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

... `description` &amp; `tax` 📦 (⏮️ 🔢 💲 `None`), 👉 🎻 "`object`" 🔜 ☑:

```JSON
{
    "name": "Foo",
    "price": 45.2
}
```

## 📣 ⚫️ 🔢

🚮 ⚫️ 👆 *➡ 🛠️*, 📣 ⚫️ 🎏 🌌 👆 📣 ➡ &amp; 🔢 🔢:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="18"
{!> ../../docs_src/body/tutorial001.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="16"
{!> ../../docs_src/body/tutorial001_py310.py!}
```

////

...&amp; 📣 🚮 🆎 🏷 👆 ✍, `Item`.

## 🏁

⏮️ 👈 🐍 🆎 📄, **ReadyAPI** 🔜:

* ✍ 💪 📨 🎻.
* 🗜 🔗 🆎 (🚥 💪).
* ✔ 💽.
    * 🚥 💽 ❌, ⚫️ 🔜 📨 👌 &amp; 🆑 ❌, ☠️ ⚫️❔ 🌐❔ &amp; ⚫️❔ ❌ 📊.
* 🤝 👆 📨 📊 🔢 `item`.
    * 👆 📣 ⚫️ 🔢 🆎 `Item`, 👆 🔜 ✔️ 🌐 👨‍🎨 🐕‍🦺 (🛠️, ♒️) 🌐 🔢 &amp; 👫 🆎.
* 🏗 <a href="https://json-schema.org" class="external-link" target="_blank">🎻 🔗</a> 🔑 👆 🏷, 👆 💪 ⚙️ 👫 🙆 🙆 👆 💖 🚥 ⚫️ ⚒ 🔑 👆 🏗.
* 👈 🔗 🔜 🍕 🏗 🗄 🔗, &amp; ⚙️ 🏧 🧾 <abbr title="User Interfaces">⚜</abbr>.

## 🏧 🩺

🎻 🔗 👆 🏷 🔜 🍕 👆 🗄 🏗 🔗, &amp; 🔜 🎦 🎓 🛠️ 🩺:

<img src="/img/tutorial/body/image01.png">

&amp; 🔜 ⚙️ 🛠️ 🩺 🔘 🔠 *➡ 🛠️* 👈 💪 👫:

<img src="/img/tutorial/body/image02.png">

## 👨‍🎨 🐕‍🦺

👆 👨‍🎨, 🔘 👆 🔢 👆 🔜 🤚 🆎 🔑 &amp; 🛠️ 🌐 (👉 🚫🔜 🔨 🚥 👆 📨 `dict` ↩️ Pydantic 🏷):

<img src="/img/tutorial/body/image03.png">

👆 🤚 ❌ ✅ ❌ 🆎 🛠️:

<img src="/img/tutorial/body/image04.png">

👉 🚫 🤞, 🎂 🛠️ 🏗 🤭 👈 🔧.

&amp; ⚫️ 🙇 💯 🔧 🌓, ⏭ 🙆 🛠️, 🚚 ⚫️ 🔜 👷 ⏮️ 🌐 👨‍🎨.

📤 🔀 Pydantic ⚫️ 🐕‍🦺 👉.

⏮️ 🖼 ✊ ⏮️ <a href="https://code.visualstudio.com" class="external-link" target="_blank">🎙 🎙 📟</a>.

✋️ 👆 🔜 🤚 🎏 👨‍🎨 🐕‍🦺 ⏮️ <a href="https://www.jetbrains.com/pycharm/" class="external-link" target="_blank">🗒</a> &amp; 🌅 🎏 🐍 👨‍🎨:

<img src="/img/tutorial/body/image05.png">

/// tip

🚥 👆 ⚙️ <a href="https://www.jetbrains.com/pycharm/" class="external-link" target="_blank">🗒</a> 👆 👨‍🎨, 👆 💪 ⚙️ <a href="https://github.com/koxudaxi/pydantic-pycharm-plugin/" class="external-link" target="_blank">Pydantic 🗒 📁</a>.

⚫️ 📉 👨‍🎨 🐕‍🦺 Pydantic 🏷, ⏮️:

* 🚘-🛠️
* 🆎 ✅
* 🛠️
* 🔎
* 🔬

///

## ⚙️ 🏷

🔘 🔢, 👆 💪 🔐 🌐 🔢 🏷 🎚 🔗:

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="21"
{!> ../../docs_src/body/tutorial002.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="19"
{!> ../../docs_src/body/tutorial002_py310.py!}
```

////

## 📨 💪 ➕ ➡ 🔢

👆 💪 📣 ➡ 🔢 &amp; 📨 💪 🎏 🕰.

**ReadyAPI** 🔜 🤔 👈 🔢 🔢 👈 🏏 ➡ 🔢 🔜 **✊ ⚪️➡️ ➡**, &amp; 👈 🔢 🔢 👈 📣 Pydantic 🏷 🔜 **✊ ⚪️➡️ 📨 💪**.

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="17-18"
{!> ../../docs_src/body/tutorial003.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="15-16"
{!> ../../docs_src/body/tutorial003_py310.py!}
```

////

## 📨 💪 ➕ ➡ ➕ 🔢 🔢

👆 💪 📣 **💪**, **➡** &amp; **🔢** 🔢, 🌐 🎏 🕰.

**ReadyAPI** 🔜 🤔 🔠 👫 &amp; ✊ 📊 ⚪️➡️ ☑ 🥉.

//// tab | 🐍 3️⃣.6️⃣ &amp; 🔛

```Python hl_lines="18"
{!> ../../docs_src/body/tutorial004.py!}
```

////

//// tab | 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛

```Python hl_lines="16"
{!> ../../docs_src/body/tutorial004_py310.py!}
```

////

🔢 🔢 🔜 🤔 ⏩:

* 🚥 🔢 📣 **➡**, ⚫️ 🔜 ⚙️ ➡ 🔢.
* 🚥 🔢 **⭐ 🆎** (💖 `int`, `float`, `str`, `bool`, ♒️) ⚫️ 🔜 🔬 **🔢** 🔢.
* 🚥 🔢 📣 🆎 **Pydantic 🏷**, ⚫️ 🔜 🔬 📨 **💪**.

/// note

ReadyAPI 🔜 💭 👈 💲 `q` 🚫 ✔ ↩️ 🔢 💲 `= None`.

 `Union` `Union[str, None]` 🚫 ⚙️ ReadyAPI, ✋️ 🔜 ✔ 👆 👨‍🎨 🤝 👆 👍 🐕‍🦺 &amp; 🔍 ❌.

///

## 🍵 Pydantic

🚥 👆 🚫 💚 ⚙️ Pydantic 🏷, 👆 💪 ⚙️ **💪** 🔢. 👀 🩺 [💪 - 💗 🔢: ⭐ 💲 💪](body-multiple-params.md#_2){.internal-link target=_blank}.
