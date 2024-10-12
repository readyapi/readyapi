# 🗄 ⏲

👆 💪 ✍ 🛠️ ⏮️ _➡ 🛠️_ 👈 💪 ⏲ 📨 _🔢 🛠️_ ✍ 👱 🙆 (🎲 🎏 👩‍💻 👈 🔜 _⚙️_ 👆 🛠️).

🛠️ 👈 🔨 🕐❔ 👆 🛠️ 📱 🤙 _🔢 🛠️_ 📛 "⏲". ↩️ 🖥 👈 🔢 👩‍💻 ✍ 📨 📨 👆 🛠️ &amp; ⤴️ 👆 🛠️ _🤙 🔙_, 📨 📨 _🔢 🛠️_ (👈 🎲 ✍ 🎏 👩‍💻).

👉 💼, 👆 💪 💚 📄 ❔ 👈 🔢 🛠️ _🔜_ 👀 💖. ⚫️❔ _➡ 🛠️_ ⚫️ 🔜 ✔️, ⚫️❔ 💪 ⚫️ 🔜 ⌛, ⚫️❔ 📨 ⚫️ 🔜 📨, ♒️.

## 📱 ⏮️ ⏲

➡️ 👀 🌐 👉 ⏮️ 🖼.

🌈 👆 🛠️ 📱 👈 ✔ 🏗 🧾.

👉 🧾 🔜 ✔️ `id`, `title` (📦), `customer`, &amp; `total`.

👩‍💻 👆 🛠️ (🔢 👩‍💻) 🔜 ✍ 🧾 👆 🛠️ ⏮️ 🏤 📨.

⤴️ 👆 🛠️ 🔜 (➡️ 🌈):

- 📨 🧾 🕴 🔢 👩‍💻.
- 📈 💸.
- 📨 📨 🔙 🛠️ 👩‍💻 (🔢 👩‍💻).
  - 👉 🔜 🔨 📨 🏤 📨 (⚪️➡️ _👆 🛠️_) _🔢 🛠️_ 🚚 👈 🔢 👩‍💻 (👉 "⏲").

## 😐 **ReadyAPI** 📱

➡️ 🥇 👀 ❔ 😐 🛠️ 📱 🔜 👀 💖 ⏭ ❎ ⏲.

⚫️ 🔜 ✔️ _➡ 🛠️_ 👈 🔜 📨 `Invoice` 💪, &amp; 🔢 🔢 `callback_url` 👈 🔜 🔌 📛 ⏲.

👉 🍕 📶 😐, 🌅 📟 🎲 ⏪ 😰 👆:

```Python hl_lines="9-13  36-53"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

/// tip

`callback_url` 🔢 🔢 ⚙️ Pydantic <a href="https://docs.pydantic.dev/latest/concepts/types/#urls" class="external-link" target="_blank">📛</a> 🆎.

///

🕴 🆕 👜 `callbacks=messages_callback_router.routes` ❌ _➡ 🛠️ 👨‍🎨_. 👥 🔜 👀 ⚫️❔ 👈 ⏭.

## 🔬 ⏲

☑ ⏲ 📟 🔜 🪀 🙇 🔛 👆 👍 🛠️ 📱.

&amp; ⚫️ 🔜 🎲 🪀 📚 ⚪️➡️ 1️⃣ 📱 ⏭.

⚫️ 💪 1️⃣ ⚖️ 2️⃣ ⏸ 📟, 💖:

```Python
callback_url = "https://example.com/api/v1/invoices/events/"
httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})
```

✋️ 🎲 🏆 ⚠ 🍕 ⏲ ⚒ 💭 👈 👆 🛠️ 👩‍💻 (🔢 👩‍💻) 🛠️ _🔢 🛠️_ ☑, 🛄 💽 👈 _👆 🛠️_ 🔜 📨 📨 💪 ⏲, ♒️.

, ⚫️❔ 👥 🔜 ⏭ 🚮 📟 📄 ❔ 👈 _🔢 🛠️_ 🔜 👀 💖 📨 ⏲ ⚪️➡️ _👆 🛠️_.

👈 🧾 🔜 🎦 🆙 🦁 🎚 `/docs` 👆 🛠️, &amp; ⚫️ 🔜 ➡️ 🔢 👩‍💻 💭 ❔ 🏗 _🔢 🛠️_.

👉 🖼 🚫 🛠️ ⏲ ⚫️ (👈 💪 ⏸ 📟), 🕴 🧾 🍕.

/// tip

☑ ⏲ 🇺🇸🔍 📨.

🕐❔ 🛠️ ⏲ 👆, 👆 💪 ⚙️ 🕳 💖 <a href="https://www.python-httpx.org" class="external-link" target="_blank">🇸🇲</a> ⚖️ <a href="https://requests.readthedocs.io/" class="external-link" target="_blank">📨</a>.

///

## ✍ ⏲ 🧾 📟

👉 📟 🏆 🚫 🛠️ 👆 📱, 👥 🕴 💪 ⚫️ _📄_ ❔ 👈 _🔢 🛠️_ 🔜 👀 💖.

✋️, 👆 ⏪ 💭 ❔ 💪 ✍ 🏧 🧾 🛠️ ⏮️ **ReadyAPI**.

👥 🔜 ⚙️ 👈 🎏 💡 📄 ❔ _🔢 🛠️_ 🔜 👀 💖... 🏗 _➡ 🛠️(Ⓜ)_ 👈 🔢 🛠️ 🔜 🛠️ (🕐 👆 🛠️ 🔜 🤙).

/// tip

🕐❔ ✍ 📟 📄 ⏲, ⚫️ 💪 ⚠ 🌈 👈 👆 👈 _🔢 👩‍💻_. &amp; 👈 👆 ⏳ 🛠️ _🔢 🛠️_, 🚫 _👆 🛠️_.

🍕 🛠️ 👉 ☝ 🎑 ( _🔢 👩‍💻_) 💪 ℹ 👆 💭 💖 ⚫️ 🌅 ⭐ 🌐❔ 🚮 🔢, Pydantic 🏷 💪, 📨, ♒️. 👈 _🔢 🛠️_.

///

### ✍ ⏲ `APIRouter`

🥇 ✍ 🆕 `APIRouter` 👈 🔜 🔌 1️⃣ ⚖️ 🌅 ⏲.

```Python hl_lines="3  25"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

### ✍ ⏲ _➡ 🛠️_

✍ ⏲ _➡ 🛠️_ ⚙️ 🎏 `APIRouter` 👆 ✍ 🔛.

⚫️ 🔜 👀 💖 😐 ReadyAPI _➡ 🛠️_:

- ⚫️ 🔜 🎲 ✔️ 📄 💪 ⚫️ 🔜 📨, ✅ `body: InvoiceEvent`.
- &amp; ⚫️ 💪 ✔️ 📄 📨 ⚫️ 🔜 📨, ✅ `response_model=InvoiceEventReceived`.

```Python hl_lines="16-18  21-22  28-32"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

📤 2️⃣ 👑 🔺 ⚪️➡️ 😐 _➡ 🛠️_:

- ⚫️ 🚫 💪 ✔️ 🙆 ☑ 📟, ↩️ 👆 📱 🔜 🙅 🤙 👉 📟. ⚫️ 🕴 ⚙️ 📄 _🔢 🛠️_. , 🔢 💪 ✔️ `pass`.
- _➡_ 💪 🔌 <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#key-expression" class="external-link" target="_blank">🗄 3️⃣ 🧬</a> (👀 🌖 🔛) 🌐❔ ⚫️ 💪 ⚙️ 🔢 ⏮️ 🔢 &amp; 🍕 ⏮️ 📨 📨 _👆 🛠️_.

### ⏲ ➡ 🧬

⏲ _➡_ 💪 ✔️ <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#key-expression" class="external-link" target="_blank">🗄 3️⃣ 🧬</a> 👈 💪 🔌 🍕 ⏮️ 📨 📨 _👆 🛠️_.

👉 💼, ⚫️ `str`:

```Python
"{$callback_url}/invoices/{$request.body.id}"
```

, 🚥 👆 🛠️ 👩‍💻 (🔢 👩‍💻) 📨 📨 _👆 🛠️_ :

```
https://yourapi.com/invoices/?callback_url=https://www.external.org/events
```

⏮️ 🎻 💪:

```JSON
{
    "id": "2expen51ve",
    "customer": "Mr. Richie Rich",
    "total": "9999"
}
```

⤴️ _👆 🛠️_ 🔜 🛠️ 🧾, &amp; ☝ ⏪, 📨 ⏲ 📨 `callback_url` ( _🔢 🛠️_):

```
https://www.external.org/events/invoices/2expen51ve
```

⏮️ 🎻 💪 ⚗ 🕳 💖:

```JSON
{
    "description": "Payment celebration",
    "paid": true
}
```

&amp; ⚫️ 🔜 ⌛ 📨 ⚪️➡️ 👈 _🔢 🛠️_ ⏮️ 🎻 💪 💖:

```JSON
{
    "ok": true
}
```

/// tip

👀 ❔ ⏲ 📛 ⚙️ 🔌 📛 📨 🔢 🔢 `callback_url` (`https://www.external.org/events`) &amp; 🧾 `id` ⚪️➡️ 🔘 🎻 💪 (`2expen51ve`).

///

### 🚮 ⏲ 📻

👉 ☝ 👆 ✔️ _⏲ ➡ 🛠️(Ⓜ)_ 💪 (1️⃣(Ⓜ) 👈 _🔢 👩‍💻_ 🔜 🛠️ _🔢 🛠️_) ⏲ 📻 👆 ✍ 🔛.

🔜 ⚙️ 🔢 `callbacks` _👆 🛠️ ➡ 🛠️ 👨‍🎨_ 🚶‍♀️ 🔢 `.routes` (👈 🤙 `list` 🛣/_➡ 🛠️_) ⚪️➡️ 👈 ⏲ 📻:

```Python hl_lines="35"
{!../../docs_src/openapi_callbacks/tutorial001.py!}
```

/// tip

👀 👈 👆 🚫 🚶‍♀️ 📻 ⚫️ (`invoices_callback_router`) `callback=`, ✋️ 🔢 `.routes`, `invoices_callback_router.routes`.

///

### ✅ 🩺

🔜 👆 💪 ▶️ 👆 📱 ⏮️ Uvicorn &amp; 🚶 <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

👆 🔜 👀 👆 🩺 ✅ "⏲" 📄 👆 _➡ 🛠️_ 👈 🎦 ❔ _🔢 🛠️_ 🔜 👀 💖:

<img src="/img/tutorial/openapi-callbacks/image01.png">
