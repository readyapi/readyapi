# 🚚 ❌

📤 📚 ⚠ 🌐❔ 👆 💪 🚨 ❌ 👩‍💻 👈 ⚙️ 👆 🛠️.

👉 👩‍💻 💪 🖥 ⏮️ 🕸, 📟 ⚪️➡️ 👱 🙆, ☁ 📳, ♒️.

👆 💪 💪 💬 👩‍💻 👈:

* 👩‍💻 🚫 ✔️ 🥃 😌 👈 🛠️.
* 👩‍💻 🚫 ✔️ 🔐 👈 ℹ.
* 🏬 👩‍💻 🔄 🔐 🚫 🔀.
* ♒️.

👫 💼, 👆 🔜 🛎 📨 **🇺🇸🔍 👔 📟** ↔ **4️⃣0️⃣0️⃣** (⚪️➡️ 4️⃣0️⃣0️⃣ 4️⃣9️⃣9️⃣).

👉 🎏 2️⃣0️⃣0️⃣ 🇺🇸🔍 👔 📟 (⚪️➡️ 2️⃣0️⃣0️⃣ 2️⃣9️⃣9️⃣). 👈 "2️⃣0️⃣0️⃣" 👔 📟 ⛓ 👈 😫 📤 "🏆" 📨.

👔 📟 4️⃣0️⃣0️⃣ ↔ ⛓ 👈 📤 ❌ ⚪️➡️ 👩‍💻.

💭 🌐 👈 **"4️⃣0️⃣4️⃣ 🚫 🔎"** ❌ (&amp; 🤣) ❓

## ⚙️ `HTTPException`

📨 🇺🇸🔍 📨 ⏮️ ❌ 👩‍💻 👆 ⚙️ `HTTPException`.

### 🗄 `HTTPException`

{* ../../examples/handling_errors/tutorial001.py hl[1] *}

### 🤚 `HTTPException` 👆 📟

`HTTPException` 😐 🐍 ⚠ ⏮️ 🌖 📊 🔗 🔗.

↩️ ⚫️ 🐍 ⚠, 👆 🚫 `return` ⚫️, 👆 `raise` ⚫️.

👉 ⛓ 👈 🚥 👆 🔘 🚙 🔢 👈 👆 🤙 🔘 👆 *➡ 🛠️ 🔢*, &amp; 👆 🤚 `HTTPException` ⚪️➡️ 🔘 👈 🚙 🔢, ⚫️ 🏆 🚫 🏃 🎂 📟 *➡ 🛠️ 🔢*, ⚫️ 🔜 ❎ 👈 📨 ▶️️ ↖️ &amp; 📨 🇺🇸🔍 ❌ ⚪️➡️ `HTTPException` 👩‍💻.

💰 🙋‍♀ ⚠ 🤭 `return`😅 💲 🔜 🌖 ⭐ 📄 🔃 🔗 &amp; 💂‍♂.

👉 🖼, 🕐❔ 👩‍💻 📨 🏬 🆔 👈 🚫 🔀, 🤚 ⚠ ⏮️ 👔 📟 `404`:

{* ../../examples/handling_errors/tutorial001.py hl[11] *}

### 📉 📨

🚥 👩‍💻 📨 `http://example.com/items/foo` ( `item_id` `"foo"`), 👈 👩‍💻 🔜 📨 🇺🇸🔍 👔 📟 2️⃣0️⃣0️⃣, &amp; 🎻 📨:

```JSON
{
  "item": "The Foo Wrestlers"
}
```

✋️ 🚥 👩‍💻 📨 `http://example.com/items/bar` (🚫-🚫 `item_id` `"bar"`), 👈 👩‍💻 🔜 📨 🇺🇸🔍 👔 📟 4️⃣0️⃣4️⃣ ("🚫 🔎" ❌), &amp; 🎻 📨:

```JSON
{
  "detail": "Item not found"
}
```

/// tip

🕐❔ 🙋‍♀ `HTTPException`, 👆 💪 🚶‍♀️ 🙆 💲 👈 💪 🗜 🎻 🔢 `detail`, 🚫 🕴 `str`.

👆 💪 🚶‍♀️ `dict`, `list`, ♒️.

👫 🍵 🔁 **ReadyAPI** &amp; 🗜 🎻.

///

## 🚮 🛃 🎚

📤 ⚠ 🌐❔ ⚫️ ⚠ 💪 🚮 🛃 🎚 🇺🇸🔍 ❌. 🖼, 🆎 💂‍♂.

👆 🎲 🏆 🚫 💪 ⚙️ ⚫️ 🔗 👆 📟.

✋️ 💼 👆 💪 ⚫️ 🏧 😐, 👆 💪 🚮 🛃 🎚:

{* ../../examples/handling_errors/tutorial002.py hl[14] *}

## ❎ 🛃 ⚠ 🐕‍🦺

👆 💪 🚮 🛃 ⚠ 🐕‍🦺 ⏮️ <a href="https://www.starlette.io/exceptions/" class="external-link" target="_blank">🎏 ⚠ 🚙 ⚪️➡️ 💃</a>.

➡️ 💬 👆 ✔️ 🛃 ⚠ `UnicornException` 👈 👆 (⚖️ 🗃 👆 ⚙️) 💪 `raise`.

&amp; 👆 💚 🍵 👉 ⚠ 🌐 ⏮️ ReadyAPI.

👆 💪 🚮 🛃 ⚠ 🐕‍🦺 ⏮️ `@app.exception_handler()`:

{* ../../examples/handling_errors/tutorial003.py hl[5:7,13:18,24] *}

📥, 🚥 👆 📨 `/unicorns/yolo`, *➡ 🛠️* 🔜 `raise` `UnicornException`.

✋️ ⚫️ 🔜 🍵 `unicorn_exception_handler`.

, 👆 🔜 📨 🧹 ❌, ⏮️ 🇺🇸🔍 👔 📟 `418` &amp; 🎻 🎚:

```JSON
{"message": "Oops! yolo did something. There goes a rainbow..."}
```

/// note | 📡 ℹ

👆 💪 ⚙️ `from starlette.requests import Request` &amp; `from starlette.responses import JSONResponse`.

**ReadyAPI** 🚚 🎏 `starlette.responses` `readyapi.responses` 🏪 👆, 👩‍💻. ✋️ 🌅 💪 📨 👟 🔗 ⚪️➡️ 💃. 🎏 ⏮️ `Request`.

///

## 🔐 🔢 ⚠ 🐕‍🦺

**ReadyAPI** ✔️ 🔢 ⚠ 🐕‍🦺.

👫 🐕‍🦺 🈚 🛬 🔢 🎻 📨 🕐❔ 👆 `raise` `HTTPException` &amp; 🕐❔ 📨 ✔️ ❌ 💽.

👆 💪 🔐 👫 ⚠ 🐕‍🦺 ⏮️ 👆 👍.

### 🔐 📨 🔬 ⚠

🕐❔ 📨 🔌 ❌ 📊, **ReadyAPI** 🔘 🤚 `RequestValidationError`.

&amp; ⚫️ 🔌 🔢 ⚠ 🐕‍🦺 ⚫️.

🔐 ⚫️, 🗄 `RequestValidationError` &amp; ⚙️ ⚫️ ⏮️ `@app.exception_handler(RequestValidationError)` 🎀 ⚠ 🐕‍🦺.

⚠ 🐕‍🦺 🔜 📨 `Request` &amp; ⚠.

{* ../../examples/handling_errors/tutorial004.py hl[2,14:16] *}

🔜, 🚥 👆 🚶 `/items/foo`, ↩️ 💆‍♂ 🔢 🎻 ❌ ⏮️:

```JSON
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

👆 🔜 🤚 ✍ ⏬, ⏮️:

```
1 validation error
path -> item_id
  value is not a valid integer (type=type_error.integer)
```

#### `RequestValidationError` 🆚 `ValidationError`

/// warning

👫 📡 ℹ 👈 👆 💪 🚶 🚥 ⚫️ 🚫 ⚠ 👆 🔜.

///

`RequestValidationError` 🎧-🎓 Pydantic <a href="https://docs.pydantic.dev/latest/concepts/models/#error-handling" class="external-link" target="_blank">`ValidationError`</a>.

**ReadyAPI** ⚙️ ⚫️ 👈, 🚥 👆 ⚙️ Pydantic 🏷 `response_model`, &amp; 👆 💽 ✔️ ❌, 👆 🔜 👀 ❌ 👆 🕹.

✋️ 👩‍💻/👩‍💻 🔜 🚫 👀 ⚫️. ↩️, 👩‍💻 🔜 📨 "🔗 💽 ❌" ⏮️ 🇺🇸🔍 👔 📟 `500`.

⚫️ 🔜 👉 🌌 ↩️ 🚥 👆 ✔️ Pydantic `ValidationError` 👆 *📨* ⚖️ 🙆 👆 📟 (🚫 👩‍💻 *📨*), ⚫️ 🤙 🐛 👆 📟.

&amp; ⏪ 👆 🔧 ⚫️, 👆 👩‍💻/👩‍💻 🚫🔜 🚫 ✔️ 🔐 🔗 ℹ 🔃 ❌, 👈 💪 🎦 💂‍♂ ⚠.

### 🔐 `HTTPException` ❌ 🐕‍🦺

🎏 🌌, 👆 💪 🔐 `HTTPException` 🐕‍🦺.

🖼, 👆 💪 💚 📨 ✅ ✍ 📨 ↩️ 🎻 👫 ❌:

{* ../../examples/handling_errors/tutorial004.py hl[3:4,9:11,22] *}

/// note | 📡 ℹ

👆 💪 ⚙️ `from starlette.responses import PlainTextResponse`.

**ReadyAPI** 🚚 🎏 `starlette.responses` `readyapi.responses` 🏪 👆, 👩‍💻. ✋️ 🌅 💪 📨 👟 🔗 ⚪️➡️ 💃.

///

### ⚙️ `RequestValidationError` 💪

`RequestValidationError` 🔌 `body` ⚫️ 📨 ⏮️ ❌ 💽.

👆 💪 ⚙️ ⚫️ ⏪ 🛠️ 👆 📱 🕹 💪 &amp; ℹ ⚫️, 📨 ⚫️ 👩‍💻, ♒️.

{* ../../examples/handling_errors/tutorial005.py hl[14] *}

🔜 🔄 📨 ❌ 🏬 💖:

```JSON
{
  "title": "towel",
  "size": "XL"
}
```

👆 🔜 📨 📨 💬 👆 👈 💽 ❌ ⚗ 📨 💪:

```JSON hl_lines="12-15"
{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "towel",
    "size": "XL"
  }
}
```

#### ReadyAPI `HTTPException` 🆚 💃 `HTTPException`

**ReadyAPI** ✔️ 🚮 👍 `HTTPException`.

&amp; **ReadyAPI**'Ⓜ `HTTPException` ❌ 🎓 😖 ⚪️➡️ 💃 `HTTPException` ❌ 🎓.

🕴 🔺, 👈 **ReadyAPI**'Ⓜ `HTTPException` ✔ 👆 🚮 🎚 🔌 📨.

👉 💪/⚙️ 🔘 ✳ 2️⃣.0️⃣ &amp; 💂‍♂ 🚙.

, 👆 💪 🚧 🙋‍♀ **ReadyAPI**'Ⓜ `HTTPException` 🛎 👆 📟.

✋️ 🕐❔ 👆 ® ⚠ 🐕‍🦺, 👆 🔜 ® ⚫️ 💃 `HTTPException`.

👉 🌌, 🚥 🙆 🍕 💃 🔗 📟, ⚖️ 💃 ↔ ⚖️ 🔌 -, 🤚 💃 `HTTPException`, 👆 🐕‍🦺 🔜 💪 ✊ &amp; 🍵 ⚫️.

👉 🖼, 💪 ✔️ 👯‍♂️ `HTTPException`Ⓜ 🎏 📟, 💃 ⚠ 📁 `StarletteHTTPException`:

```Python
from starlette.exceptions import HTTPException as StarletteHTTPException
```

### 🏤-⚙️ **ReadyAPI**'Ⓜ ⚠ 🐕‍🦺

🚥 👆 💚 ⚙️ ⚠ ⤴️ ⏮️ 🎏 🔢 ⚠ 🐕‍🦺 ⚪️➡️ **ReadyAPI**, 👆 💪 🗄 &amp; 🏤-⚙️ 🔢 ⚠ 🐕‍🦺 ⚪️➡️ `readyapi.exception_handlers`:

{* ../../examples/handling_errors/tutorial006.py hl[2:5,15,21] *}

👉 🖼 👆 `print`😅 ❌ ⏮️ 📶 🎨 📧, ✋️ 👆 🤚 💭. 👆 💪 ⚙️ ⚠ &amp; ⤴️ 🏤-⚙️ 🔢 ⚠ 🐕‍🦺.
