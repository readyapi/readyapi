# 📄

👆 💪 ⚙️ 🙆 📄 🚒 👆 💚 ⏮️ **ReadyAPI**.

⚠ ⚒ Jinja2️⃣, 🎏 1️⃣ ⚙️ 🏺 &amp; 🎏 🧰.

📤 🚙 🔗 ⚫️ 💪 👈 👆 💪 ⚙️ 🔗 👆 **ReadyAPI** 🈸 (🚚 💃).

## ❎ 🔗

❎ `jinja2`:

<div class="termy">

```console
$ pip install jinja2

---> 100%
```

</div>

## ⚙️ `Jinja2Templates`

* 🗄 `Jinja2Templates`.
* ✍ `templates` 🎚 👈 👆 💪 🏤-⚙️ ⏪.
* 📣 `Request` 🔢 *➡ 🛠️* 👈 🔜 📨 📄.
* ⚙️ `templates` 👆 ✍ ✍ &amp; 📨 `TemplateResponse`, 🚶‍♀️ `request` 1️⃣ 🔑-💲 👫 Jinja2️⃣ "🔑".

{* ../../examples/templates/tutorial001.py hl[4,11,15:18] *}

/// note

👀 👈 👆 ✔️ 🚶‍♀️ `request` 🍕 🔑-💲 👫 🔑 Jinja2️⃣. , 👆 ✔️ 📣 ⚫️ 👆 *➡ 🛠️*.

///

/// tip

📣 `response_class=HTMLResponse` 🩺 🎚 🔜 💪 💭 👈 📨 🔜 🕸.

///

/// note | 📡 ℹ

👆 💪 ⚙️ `from starlette.templating import Jinja2Templates`.

**ReadyAPI** 🚚 🎏 `starlette.templating` `readyapi.templating` 🏪 👆, 👩‍💻. ✋️ 🌅 💪 📨 👟 🔗 ⚪️➡️ 💃. 🎏 ⏮️ `Request` &amp; `StaticFiles`.

///

## ✍ 📄

⤴️ 👆 💪 ✍ 📄 `templates/item.html` ⏮️:

```jinja hl_lines="7"
{!../../examples/templates/templates/item.html!}
```

⚫️ 🔜 🎦 `id` ✊ ⚪️➡️ "🔑" `dict` 👆 🚶‍♀️:

```Python
{"request": request, "id": id}
```

## 📄 &amp; 🎻 📁

&amp; 👆 💪 ⚙️ `url_for()` 🔘 📄, &amp; ⚙️ ⚫️, 🖼, ⏮️ `StaticFiles` 👆 📌.

```jinja hl_lines="4"
{!../../examples/templates/templates/item.html!}
```

👉 🖼, ⚫️ 🔜 🔗 🎚 📁 `static/styles.css` ⏮️:

```CSS hl_lines="4"
{!../../examples/templates/static/styles.css!}
```

&amp; ↩️ 👆 ⚙️ `StaticFiles`, 👈 🎚 📁 🔜 🍦 🔁 👆 **ReadyAPI** 🈸 📛 `/static/styles.css`.

## 🌅 ℹ

🌅 ℹ, 🔌 ❔ 💯 📄, ✅ <a href="https://www.starlette.io/templates/" class="external-link" target="_blank">💃 🩺 🔛 📄</a>.
