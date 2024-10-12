# ➡ 🛠️ 🏧 📳

## 🗄 {

/// warning

🚥 👆 🚫 "🕴" 🗄, 👆 🎲 🚫 💪 👉.

///

👆 💪 ⚒ 🗄 `operationId` ⚙️ 👆 _➡ 🛠️_ ⏮️ 🔢 `operation_id`.

👆 🔜 ✔️ ⚒ 💭 👈 ⚫️ 😍 🔠 🛠️.

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial001.py!}
```

### ⚙️ _➡ 🛠️ 🔢_ 📛 {

🚥 👆 💚 ⚙️ 👆 🔗' 🔢 📛 `operationId`Ⓜ, 👆 💪 🔁 🤭 🌐 👫 &amp; 🔐 🔠 _➡ 🛠️_ `operation_id` ⚙️ 👫 `APIRoute.name`.

👆 🔜 ⚫️ ⏮️ ❎ 🌐 👆 _➡ 🛠️_.

```Python hl_lines="2  12-21  24"
{!../../docs_src/path_operation_advanced_configuration/tutorial002.py!}
```

/// tip

🚥 👆 ❎ 🤙 `app.openapi()`, 👆 🔜 ℹ `operationId`Ⓜ ⏭ 👈.

///

/// warning

🚥 👆 👉, 👆 ✔️ ⚒ 💭 🔠 1️⃣ 👆 _➡ 🛠️ 🔢_ ✔️ 😍 📛.

🚥 👫 🎏 🕹 (🐍 📁).

///

## 🚫 ⚪️➡️ 🗄

🚫 _➡ 🛠️_ ⚪️➡️ 🏗 🗄 🔗 (&amp; ➡️, ⚪️➡️ 🏧 🧾 ⚙️), ⚙️ 🔢 `include_in_schema` &amp; ⚒ ⚫️ `False`:

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial003.py!}
```

## 🏧 📛 ⚪️➡️ #️⃣

👆 💪 📉 ⏸ ⚙️ ⚪️➡️ #️⃣ _➡ 🛠️ 🔢_ 🗄.

❎ `\f` (😖 "📨 🍼" 🦹) 🤕 **ReadyAPI** 🔁 🔢 ⚙️ 🗄 👉 ☝.

⚫️ 🏆 🚫 🎦 🆙 🧾, ✋️ 🎏 🧰 (✅ 🐉) 🔜 💪 ⚙️ 🎂.

```Python hl_lines="19-29"
{!../../docs_src/path_operation_advanced_configuration/tutorial004.py!}
```

## 🌖 📨

👆 🎲 ✔️ 👀 ❔ 📣 `response_model` &amp; `status_code` _➡ 🛠️_.

👈 🔬 🗃 🔃 👑 📨 _➡ 🛠️_.

👆 💪 📣 🌖 📨 ⏮️ 👫 🏷, 👔 📟, ♒️.

📤 🎂 📃 📥 🧾 🔃 ⚫️, 👆 💪 ✍ ⚫️ [🌖 📨 🗄](additional-responses.md){.internal-link target=\_blank}.

## 🗄 ➕

🕐❔ 👆 📣 _➡ 🛠️_ 👆 🈸, **ReadyAPI** 🔁 🏗 🔗 🗃 🔃 👈 _➡ 🛠️_ 🔌 🗄 🔗.

/// note | "📡 ℹ"

🗄 🔧 ⚫️ 🤙 <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object" class="external-link" target="_blank">🛠️ 🎚</a>.

///

⚫️ ✔️ 🌐 ℹ 🔃 _➡ 🛠️_ &amp; ⚙️ 🏗 🏧 🧾.

⚫️ 🔌 `tags`, `parameters`, `requestBody`, `responses`, ♒️.

👉 _➡ 🛠️_-🎯 🗄 🔗 🛎 🏗 🔁 **ReadyAPI**, ✋️ 👆 💪 ↔ ⚫️.

/// tip

👉 🔅 🎚 ↔ ☝.

🚥 👆 🕴 💪 📣 🌖 📨, 🌅 🏪 🌌 ⚫️ ⏮️ [🌖 📨 🗄](additional-responses.md){.internal-link target=\_blank}.

///

👆 💪 ↔ 🗄 🔗 _➡ 🛠️_ ⚙️ 🔢 `openapi_extra`.

### 🗄 ↔

👉 `openapi_extra` 💪 👍, 🖼, 📣 [🗄 ↔](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#specificationExtensions):

```Python hl_lines="6"
{!../../docs_src/path_operation_advanced_configuration/tutorial005.py!}
```

🚥 👆 📂 🏧 🛠️ 🩺, 👆 ↔ 🔜 🎦 🆙 🔝 🎯 _➡ 🛠️_.

<img src="/img/tutorial/path-operation-advanced-configuration/image01.png">

&amp; 🚥 👆 👀 📉 🗄 ( `/openapi.json` 👆 🛠️), 👆 🔜 👀 👆 ↔ 🍕 🎯 _➡ 🛠️_ 💁‍♂️:

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

### 🛃 🗄 _➡ 🛠️_ 🔗

📖 `openapi_extra` 🔜 🙇 🔗 ⏮️ 🔁 🏗 🗄 🔗 _➡ 🛠️_.

, 👆 💪 🚮 🌖 💽 🔁 🏗 🔗.

🖼, 👆 💪 💭 ✍ &amp; ✔ 📨 ⏮️ 👆 👍 📟, 🍵 ⚙️ 🏧 ⚒ ReadyAPI ⏮️ Pydantic, ✋️ 👆 💪 💚 🔬 📨 🗄 🔗.

👆 💪 👈 ⏮️ `openapi_extra`:

```Python hl_lines="20-37  39-40"
{!../../docs_src/path_operation_advanced_configuration/tutorial006.py!}
```

👉 🖼, 👥 🚫 📣 🙆 Pydantic 🏷. 👐, 📨 💪 🚫 <abbr title="converted from some plain format, like bytes, into Python objects">🎻</abbr> 🎻, ⚫️ ✍ 🔗 `bytes`, &amp; 🔢 `magic_data_reader()` 🔜 🈚 🎻 ⚫️ 🌌.

👐, 👥 💪 📣 📈 🔗 📨 💪.

### 🛃 🗄 🎚 🆎

⚙️ 👉 🎏 🎱, 👆 💪 ⚙️ Pydantic 🏷 🔬 🎻 🔗 👈 ⤴️ 🔌 🛃 🗄 🔗 📄 _➡ 🛠️_.

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
