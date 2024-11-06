# ➡ 🛠️ 🏧 📳

## 🗄 {

/// warning

🚥 👆 🚫 "🕴" 🗄, 👆 🎲 🚫 💪 👉.

///

👆 💪 ⚒ 🗄 `operationId` ⚙️ 👆 *➡ 🛠️* ⏮️ 🔢 `operation_id`.

👆 🔜 ✔️ ⚒ 💭 👈 ⚫️ 😍 🔠 🛠️.

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial001.py!}
```

### ⚙️ *➡ 🛠️ 🔢* 📛 {

🚥 👆 💚 ⚙️ 👆 🔗' 🔢 📛 `operationId`Ⓜ, 👆 💪 🔁 🤭 🌐 👫 &amp; 🔐 🔠 *➡ 🛠️* `operation_id` ⚙️ 👫 `APIRoute.name`.

👆 🔜 ⚫️ ⏮️ ❎ 🌐 👆 *➡ 🛠️*.

```Python hl_lines="2  12-21  24"
{!../../docs_src/path_operation_advanced_configuration/tutorial002.py!}
```

/// tip

🚥 👆 ❎ 🤙 `app.openapi()`, 👆 🔜 ℹ `operationId`Ⓜ ⏭ 👈.

///

/// warning

🚥 👆 👉, 👆 ✔️ ⚒ 💭 🔠 1️⃣ 👆 *➡ 🛠️ 🔢* ✔️ 😍 📛.

🚥 👫 🎏 🕹 (🐍 📁).

///

## 🚫 ⚪️➡️ 🗄

🚫 *➡ 🛠️* ⚪️➡️ 🏗 🗄 🔗 (&amp; ➡️, ⚪️➡️ 🏧 🧾 ⚙️), ⚙️ 🔢 `include_in_schema` &amp; ⚒ ⚫️ `False`:

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial003.py!}
```

## 🏧 📛 ⚪️➡️ #️⃣

👆 💪 📉 ⏸ ⚙️ ⚪️➡️ #️⃣ *➡ 🛠️ 🔢* 🗄.

❎ `\f` (😖 "📨 🍼" 🦹) 🤕 **ReadyAPI** 🔁 🔢 ⚙️ 🗄 👉 ☝.

⚫️ 🏆 🚫 🎦 🆙 🧾, ✋️ 🎏 🧰 (✅ 🐉) 🔜 💪 ⚙️ 🎂.

```Python hl_lines="19-29"
{!../../docs_src/path_operation_advanced_configuration/tutorial004.py!}
```

## 🌖 📨

👆 🎲 ✔️ 👀 ❔ 📣 `response_model` &amp; `status_code` *➡ 🛠️*.

👈 🔬 🗃 🔃 👑 📨 *➡ 🛠️*.

👆 💪 📣 🌖 📨 ⏮️ 👫 🏷, 👔 📟, ♒️.

📤 🎂 📃 📥 🧾 🔃 ⚫️, 👆 💪 ✍ ⚫️ [🌖 📨 🗄](additional-responses.md){.internal-link target=_blank}.

## 🗄 ➕

🕐❔ 👆 📣 *➡ 🛠️* 👆 🈸, **ReadyAPI** 🔁 🏗 🔗 🗃 🔃 👈 *➡ 🛠️* 🔌 🗄 🔗.

/// note | "📡 ℹ"

🗄 🔧 ⚫️ 🤙 <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object" class="external-link" target="_blank">🛠️ 🎚</a>.

///

⚫️ ✔️ 🌐 ℹ 🔃 *➡ 🛠️* &amp; ⚙️ 🏗 🏧 🧾.

⚫️ 🔌 `tags`, `parameters`, `requestBody`, `responses`, ♒️.

👉 *➡ 🛠️*-🎯 🗄 🔗 🛎 🏗 🔁 **ReadyAPI**, ✋️ 👆 💪 ↔ ⚫️.

/// tip

👉 🔅 🎚 ↔ ☝.

🚥 👆 🕴 💪 📣 🌖 📨, 🌅 🏪 🌌 ⚫️ ⏮️ [🌖 📨 🗄](additional-responses.md){.internal-link target=_blank}.

///

👆 💪 ↔ 🗄 🔗 *➡ 🛠️* ⚙️ 🔢 `openapi_extra`.

### 🗄 ↔

👉 `openapi_extra` 💪 👍, 🖼, 📣 [🗄 ↔](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#specificationExtensions):

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial005.py!}
```

🚥 👆 📂 🏧 🛠️ 🩺, 👆 ↔ 🔜 🎦 🆙 🔝 🎯 *➡ 🛠️*.

<img src="/img/tutorial/path-operation-advanced-configuration/image01.png">

&amp; 🚥 👆 👀 📉 🗄 ( `/openapi.json` 👆 🛠️), 👆 🔜 👀 👆 ↔ 🍕 🎯 *➡ 🛠️* 💁‍♂️:

```JSON hl_lines="22"
{
    "openapi": "3.0.2",
    "info": {
        "title": "ReadyAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "summary": "Read Items",
                "operationId": "read_items_items__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "x-aperture-labs-portal": "blue"
            }
        }
    }
}
```

### 🛃 🗄 *➡ 🛠️* 🔗

📖 `openapi_extra` 🔜 🙇 🔗 ⏮️ 🔁 🏗 🗄 🔗 *➡ 🛠️*.

, 👆 💪 🚮 🌖 💽 🔁 🏗 🔗.

🖼, 👆 💪 💭 ✍ &amp; ✔ 📨 ⏮️ 👆 👍 📟, 🍵 ⚙️ 🏧 ⚒ ReadyAPI ⏮️ Pydantic, ✋️ 👆 💪 💚 🔬 📨 🗄 🔗.

👆 💪 👈 ⏮️ `openapi_extra`:

```Python hl_lines="20-37  39-40"
{!../../docs_src/path_operation_advanced_configuration/tutorial006.py!}
```

👉 🖼, 👥 🚫 📣 🙆 Pydantic 🏷. 👐, 📨 💪 🚫 <abbr title="converted from some plain format, like bytes, into Python objects">🎻</abbr> 🎻, ⚫️ ✍ 🔗 `bytes`, &amp; 🔢 `magic_data_reader()` 🔜 🈚 🎻 ⚫️ 🌌.

👐, 👥 💪 📣 📈 🔗 📨 💪.

### 🛃 🗄 🎚 🆎

⚙️ 👉 🎏 🎱, 👆 💪 ⚙️ Pydantic 🏷 🔬 🎻 🔗 👈 ⤴️ 🔌 🛃 🗄 🔗 📄 *➡ 🛠️*.

&amp; 👆 💪 👉 🚥 💽 🆎 📨 🚫 🎻.

🖼, 👉 🈸 👥 🚫 ⚙️ ReadyAPI 🛠️ 🛠️ ⚗ 🎻 🔗 ⚪️➡️ Pydantic 🏷 🚫 🏧 🔬 🎻. 👐, 👥 📣 📨 🎚 🆎 📁, 🚫 🎻:

```Python hl_lines="17-22  24"
{!../../docs_src/path_operation_advanced_configuration/tutorial007.py!}
```

👐, 👐 👥 🚫 ⚙️ 🔢 🛠️ 🛠️, 👥 ⚙️ Pydantic 🏷 ❎ 🏗 🎻 🔗 💽 👈 👥 💚 📨 📁.

⤴️ 👥 ⚙️ 📨 🔗, &amp; ⚗ 💪 `bytes`. 👉 ⛓ 👈 ReadyAPI 🏆 🚫 🔄 🎻 📨 🚀 🎻.

&amp; ⤴️ 👆 📟, 👥 🎻 👈 📁 🎚 🔗, &amp; ⤴️ 👥 🔄 ⚙️ 🎏 Pydantic 🏷 ✔ 📁 🎚:

```Python hl_lines="26-33"
{!../../docs_src/path_operation_advanced_configuration/tutorial007.py!}
```

/// tip

📥 👥 🏤-⚙️ 🎏 Pydantic 🏷.

✋️ 🎏 🌌, 👥 💪 ✔️ ✔ ⚫️ 🎏 🌌.

///
