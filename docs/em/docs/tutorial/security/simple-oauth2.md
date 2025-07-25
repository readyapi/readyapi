# 🙅 Oauth2️⃣ ⏮️ 🔐 &amp; 📨

🔜 ➡️ 🏗 ⚪️➡️ ⏮️ 📃 &amp; 🚮 ❌ 🍕 ✔️ 🏁 💂‍♂ 💧.

## 🤚 `username` &amp; `password`

👥 🔜 ⚙️ **ReadyAPI** 💂‍♂ 🚙 🤚 `username` &amp; `password`.

Oauth2️⃣ ✔ 👈 🕐❔ ⚙️ "🔐 💧" (👈 👥 ⚙️) 👩‍💻/👩‍💻 🔜 📨 `username` &amp; `password` 🏑 📨 💽.

&amp; 🔌 💬 👈 🏑 ✔️ 🌟 💖 👈. `user-name` ⚖️ `email` 🚫🔜 👷.

✋️ 🚫 😟, 👆 💪 🎦 ⚫️ 👆 🎋 👆 🏁 👩‍💻 🕸.

&amp; 👆 💽 🏷 💪 ⚙️ 🙆 🎏 📛 👆 💚.

✋️ 💳 *➡ 🛠️*, 👥 💪 ⚙️ 👉 📛 🔗 ⏮️ 🔌 (&amp; 💪, 🖼, ⚙️ 🛠️ 🛠️ 🧾 ⚙️).

🔌 🇵🇸 👈 `username` &amp; `password` 🔜 📨 📨 💽 (, 🙅‍♂ 🎻 📥).

### `scope`

🔌 💬 👈 👩‍💻 💪 📨 ➕1️⃣ 📨 🏑 "`scope`".

📨 🏑 📛 `scope` (⭐), ✋️ ⚫️ 🤙 📏 🎻 ⏮️ "↔" 🎏 🚀.

🔠 "↔" 🎻 (🍵 🚀).

👫 🛎 ⚙️ 📣 🎯 💂‍♂ ✔, 🖼:

* `users:read` ⚖️ `users:write` ⚠ 🖼.
* `instagram_basic` ⚙️ 👱📔 / 👱📔.
* `https://www.googleapis.com/auth/drive` ⚙️ 🇺🇸🔍.

/// info

Oauth2️⃣ "↔" 🎻 👈 📣 🎯 ✔ ✔.

⚫️ 🚫 🤔 🚥 ⚫️ ✔️ 🎏 🦹 💖 `:` ⚖️ 🚥 ⚫️ 📛.

👈 ℹ 🛠️ 🎯.

Oauth2️⃣ 👫 🎻.

///

## 📟 🤚 `username` &amp; `password`

🔜 ➡️ ⚙️ 🚙 🚚 **ReadyAPI** 🍵 👉.

### `OAuth2PasswordRequestForm`

🥇, 🗄 `OAuth2PasswordRequestForm`, &amp; ⚙️ ⚫️ 🔗 ⏮️ `Depends` *➡ 🛠️* `/token`:

{* ../../examples/security/tutorial003.py hl[4,76] *}

`OAuth2PasswordRequestForm` 🎓 🔗 👈 📣 📨 💪 ⏮️:

*  `username`.
*  `password`.
* 📦 `scope` 🏑 🦏 🎻, ✍ 🎻 🎏 🚀.
* 📦 `grant_type`.

/// tip

Oauth2️⃣ 🔌 🤙 *🚚* 🏑 `grant_type` ⏮️ 🔧 💲 `password`, ✋️ `OAuth2PasswordRequestForm` 🚫 🛠️ ⚫️.

🚥 👆 💪 🛠️ ⚫️, ⚙️ `OAuth2PasswordRequestFormStrict` ↩️ `OAuth2PasswordRequestForm`.

///

* 📦 `client_id` (👥 🚫 💪 ⚫️ 👆 🖼).
* 📦 `client_secret` (👥 🚫 💪 ⚫️ 👆 🖼).

/// info

`OAuth2PasswordRequestForm` 🚫 🎁 🎓 **ReadyAPI** `OAuth2PasswordBearer`.

`OAuth2PasswordBearer` ⚒ **ReadyAPI** 💭 👈 ⚫️ 💂‍♂ ⚖. ⚫️ 🚮 👈 🌌 🗄.

✋️ `OAuth2PasswordRequestForm` 🎓 🔗 👈 👆 💪 ✔️ ✍ 👆, ⚖️ 👆 💪 ✔️ 📣 `Form` 🔢 🔗.

✋️ ⚫️ ⚠ ⚙️ 💼, ⚫️ 🚚 **ReadyAPI** 🔗, ⚒ ⚫️ ⏩.

///

### ⚙️ 📨 💽

/// tip

👐 🔗 🎓 `OAuth2PasswordRequestForm` 🏆 🚫 ✔️ 🔢 `scope` ⏮️ 📏 🎻 👽 🚀, ↩️, ⚫️ 🔜 ✔️ `scopes` 🔢 ⏮️ ☑ 📇 🎻 🔠 ↔ 📨.

👥 🚫 ⚙️ `scopes` 👉 🖼, ✋️ 🛠️ 📤 🚥 👆 💪 ⚫️.

///

🔜, 🤚 👩‍💻 📊 ⚪️➡️ (❌) 💽, ⚙️ `username` ⚪️➡️ 📨 🏑.

🚥 📤 🙅‍♂ ✅ 👩‍💻, 👥 📨 ❌ 💬 "❌ 🆔 ⚖️ 🔐".

❌, 👥 ⚙️ ⚠ `HTTPException`:

{* ../../examples/security/tutorial003.py hl[3,77:79] *}

### ✅ 🔐

👉 ☝ 👥 ✔️ 👩‍💻 📊 ⚪️➡️ 👆 💽, ✋️ 👥 🚫 ✅ 🔐.

➡️ 🚮 👈 💽 Pydantic `UserInDB` 🏷 🥇.

👆 🔜 🙅 🖊 🔢 🔐,, 👥 🔜 ⚙️ (❌) 🔐 🔁 ⚙️.

🚥 🔐 🚫 🏏, 👥 📨 🎏 ❌.

#### 🔐 🔁

"🔁" ⛓: 🏭 🎚 (🔐 👉 💼) 🔘 🔁 🔢 (🎻) 👈 👀 💖 🙃.

🕐❔ 👆 🚶‍♀️ ⚫️❔ 🎏 🎚 (⚫️❔ 🎏 🔐) 👆 🤚 ⚫️❔ 🎏 🙃.

✋️ 👆 🚫🔜 🗜 ⚪️➡️ 🙃 🔙 🔐.

##### ⚫️❔ ⚙️ 🔐 🔁

🚥 👆 💽 📎, 🧙‍♀ 🏆 🚫 ✔️ 👆 👩‍💻' 🔢 🔐, 🕴#️⃣.

, 🧙‍♀ 🏆 🚫 💪 🔄 ⚙️ 👈 🎏 🔐 ➕1️⃣ ⚙️ (📚 👩‍💻 ⚙️ 🎏 🔐 🌐, 👉 🔜 ⚠).

{* ../../examples/security/tutorial003.py hl[80:83] *}

#### 🔃 `**user_dict`

`UserInDB(**user_dict)` ⛓:

*🚶‍♀️ 🔑 &amp; 💲 `user_dict` 🔗 🔑-💲 ❌, 🌓:*

```Python
UserInDB(
    username = user_dict["username"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    disabled = user_dict["disabled"],
    hashed_password = user_dict["hashed_password"],
)
```

/// info

🌅 🏁 🔑 `**👩‍💻_ #️⃣ ` ✅ 🔙 [🧾 **➕ 🏷**](../extra-models.md#user_indict){.internal-link target=_blank}.

///

## 📨 🤝

📨 `token` 🔗 🔜 🎻 🎚.

⚫️ 🔜 ✔️ `token_type`. 👆 💼, 👥 ⚙️ "📨" 🤝, 🤝 🆎 🔜 "`bearer`".

&amp; ⚫️ 🔜 ✔️ `access_token`, ⏮️ 🎻 ⚗ 👆 🔐 🤝.

👉 🙅 🖼, 👥 🔜 🍕 😟 &amp; 📨 🎏 `username` 🤝.

/// tip

⏭ 📃, 👆 🔜 👀 🎰 🔐 🛠️, ⏮️ 🔐 #️⃣ &amp; <abbr title="JSON Web Tokens">🥙</abbr> 🤝.

✋️ 🔜, ➡️ 🎯 🔛 🎯 ℹ 👥 💪.

///

{* ../../examples/security/tutorial003.py hl[85] *}

/// tip

🔌, 👆 🔜 📨 🎻 ⏮️ `access_token` &amp; `token_type`, 🎏 👉 🖼.

👉 🕳 👈 👆 ✔️ 👆 👆 📟, &amp; ⚒ 💭 👆 ⚙️ 📚 🎻 🔑.

⚫️ 🌖 🕴 👜 👈 👆 ✔️ 💭 ☑ 👆, 🛠️ ⏮️ 🔧.

🎂, **ReadyAPI** 🍵 ⚫️ 👆.

///

## ℹ 🔗

🔜 👥 🔜 ℹ 👆 🔗.

👥 💚 🤚 `current_user` *🕴* 🚥 👉 👩‍💻 🦁.

, 👥 ✍ 🌖 🔗 `get_current_active_user` 👈 🔄 ⚙️ `get_current_user` 🔗.

👯‍♂️ 👉 🔗 🔜 📨 🇺🇸🔍 ❌ 🚥 👩‍💻 🚫 🔀, ⚖️ 🚥 🔕.

, 👆 🔗, 👥 🔜 🕴 🤚 👩‍💻 🚥 👩‍💻 🔀, ☑ 🔓, &amp; 🦁:

{* ../../examples/security/tutorial003.py hl[58:66,69:72,90] *}

/// info

🌖 🎚 `WWW-Authenticate` ⏮️ 💲 `Bearer` 👥 🛬 📥 🍕 🔌.

🙆 🇺🇸🔍 (❌) 👔 📟 4️⃣0️⃣1️⃣ "⛔" 🤔 📨 `WWW-Authenticate` 🎚.

💼 📨 🤝 (👆 💼), 💲 👈 🎚 🔜 `Bearer`.

👆 💪 🤙 🚶 👈 ➕ 🎚 &amp; ⚫️ 🔜 👷.

✋️ ⚫️ 🚚 📥 🛠️ ⏮️ 🔧.

, 📤 5️⃣📆 🧰 👈 ⌛ &amp; ⚙️ ⚫️ (🔜 ⚖️ 🔮) &amp; 👈 💪 ⚠ 👆 ⚖️ 👆 👩‍💻, 🔜 ⚖️ 🔮.

👈 💰 🐩...

///

## 👀 ⚫️ 🎯

📂 🎓 🩺: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

### 🔓

🖊 "✔" 🔼.

⚙️ 🎓:

👩‍💻: `johndoe`

🔐: `secret`

<img src="/img/tutorial/security/image04.png">

⏮️ 🔗 ⚙️, 👆 🔜 👀 ⚫️ 💖:

<img src="/img/tutorial/security/image05.png">

### 🤚 👆 👍 👩‍💻 💽

🔜 ⚙️ 🛠️ `GET` ⏮️ ➡ `/users/me`.

👆 🔜 🤚 👆 👩‍💻 📊, 💖:

```JSON
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false,
  "hashed_password": "fakehashedsecret"
}
```

<img src="/img/tutorial/security/image06.png">

🚥 👆 🖊 🔒 ℹ &amp; ⏏, &amp; ⤴️ 🔄 🎏 🛠️ 🔄, 👆 🔜 🤚 🇺🇸🔍 4️⃣0️⃣1️⃣ ❌:

```JSON
{
  "detail": "Not authenticated"
}
```

### 🔕 👩‍💻

🔜 🔄 ⏮️ 🔕 👩‍💻, 🔓 ⏮️:

👩‍💻: `alice`

🔐: `secret2`

&amp; 🔄 ⚙️ 🛠️ `GET` ⏮️ ➡ `/users/me`.

👆 🔜 🤚 "🔕 👩‍💻" ❌, 💖:

```JSON
{
  "detail": "Inactive user"
}
```

## 🌃

👆 🔜 ✔️ 🧰 🛠️ 🏁 💂‍♂ ⚙️ ⚓️ 🔛 `username` &amp; `password` 👆 🛠️.

⚙️ 👫 🧰, 👆 💪 ⚒ 💂‍♂ ⚙️ 🔗 ⏮️ 🙆 💽 &amp; ⏮️ 🙆 👩‍💻 ⚖️ 💽 🏷.

🕴 ℹ ❌ 👈 ⚫️ 🚫 🤙 "🔐".

⏭ 📃 👆 🔜 👀 ❔ ⚙️ 🔐 🔐 🔁 🗃 &amp; <abbr title="JSON Web Tokens">🥙</abbr> 🤝.
