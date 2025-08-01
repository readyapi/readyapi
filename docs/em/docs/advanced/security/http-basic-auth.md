# 🇺🇸🔍 🔰 🔐

🙅 💼, 👆 💪 ⚙️ 🇺🇸🔍 🔰 🔐.

🇺🇸🔍 🔰 🔐, 🈸 ⌛ 🎚 👈 🔌 🆔 &amp; 🔐.

🚥 ⚫️ 🚫 📨 ⚫️, ⚫️ 📨 🇺🇸🔍 4️⃣0️⃣1️⃣ "⛔" ❌.

&amp; 📨 🎚 `WWW-Authenticate` ⏮️ 💲 `Basic`, &amp; 📦 `realm` 🔢.

👈 💬 🖥 🎦 🛠️ 📋 🆔 &amp; 🔐.

⤴️, 🕐❔ 👆 🆎 👈 🆔 &amp; 🔐, 🖥 📨 👫 🎚 🔁.

## 🙅 🇺🇸🔍 🔰 🔐

* 🗄 `HTTPBasic` &amp; `HTTPBasicCredentials`.
* ✍ "`security` ⚖" ⚙️ `HTTPBasic`.
* ⚙️ 👈 `security` ⏮️ 🔗 👆 *➡ 🛠️*.
* ⚫️ 📨 🎚 🆎 `HTTPBasicCredentials`:
    * ⚫️ 🔌 `username` &amp; `password` 📨.

{* ../../examples/security/tutorial006.py hl[2,6,10] *}

🕐❔ 👆 🔄 📂 📛 🥇 🕰 (⚖️ 🖊 "🛠️" 🔼 🩺) 🖥 🔜 💭 👆 👆 🆔 &amp; 🔐:

<img src="/img/tutorial/security/image12.png">

## ✅ 🆔

📥 🌅 🏁 🖼.

⚙️ 🔗 ✅ 🚥 🆔 &amp; 🔐 ☑.

👉, ⚙️ 🐍 🐩 🕹 <a href="https://docs.python.org/3/library/secrets.html" class="external-link" target="_blank">`secrets`</a> ✅ 🆔 &amp; 🔐.

`secrets.compare_digest()` 💪 ✊ `bytes` ⚖️ `str` 👈 🕴 🔌 🔠 🦹 (🕐 🇪🇸), 👉 ⛓ ⚫️ 🚫🔜 👷 ⏮️ 🦹 💖 `á`, `KhulnaSoft`.

🍵 👈, 👥 🥇 🗜 `username` &amp; `password` `bytes` 🔢 👫 ⏮️ 🔠-8️⃣.

⤴️ 👥 💪 ⚙️ `secrets.compare_digest()` 🚚 👈 `credentials.username` `"stanleyjobson"`, &amp; 👈 `credentials.password` `"swordfish"`.

{* ../../examples/security/tutorial007.py hl[1,11:21] *}

👉 🔜 🎏:

```Python
if not (credentials.username == "stanleyjobson") or not (credentials.password == "swordfish"):
    # Return some error
    ...
```

✋️ ⚙️ `secrets.compare_digest()` ⚫️ 🔜 🔐 🛡 🆎 👊 🤙 "🕰 👊".

### ⏲ 👊

✋️ ⚫️❔ "⏲ 👊"❓

➡️ 🌈 👊 🔄 💭 🆔 &amp; 🔐.

&amp; 👫 📨 📨 ⏮️ 🆔 `johndoe` &amp; 🔐 `love123`.

⤴️ 🐍 📟 👆 🈸 🔜 🌓 🕳 💖:

```Python
if "johndoe" == "stanleyjobson" and "love123" == "swordfish":
    ...
```

✋️ ▶️️ 🙍 🐍 🔬 🥇 `j` `johndoe` 🥇 `s` `stanleyjobson`, ⚫️ 🔜 📨 `False`, ↩️ ⚫️ ⏪ 💭 👈 📚 2️⃣ 🎻 🚫 🎏, 💭 👈 "📤 🙅‍♂ 💪 🗑 🌅 📊 ⚖ 🎂 🔤". &amp; 👆 🈸 🔜 💬 "❌ 👩‍💻 ⚖️ 🔐".

✋️ ⤴️ 👊 🔄 ⏮️ 🆔 `stanleyjobsox` &amp; 🔐 `love123`.

&amp; 👆 🈸 📟 🔨 🕳 💖:

```Python
if "stanleyjobsox" == "stanleyjobson" and "love123" == "swordfish":
    ...
```

🐍 🔜 ✔️ 🔬 🎂 `stanleyjobso` 👯‍♂️ `stanleyjobsox` &amp; `stanleyjobson` ⏭ 🤔 👈 👯‍♂️ 🎻 🚫 🎏. ⚫️ 🔜 ✊ ➕ ⏲ 📨 🔙 "❌ 👩‍💻 ⚖️ 🔐".

#### 🕰 ❔ ℹ 👊

👈 ☝, 👀 👈 💽 ✊ ⏲ 📏 📨 "❌ 👩‍💻 ⚖️ 🔐" 📨, 👊 🔜 💭 👈 👫 🤚 _🕳_ ▶️️, ▶️ 🔤 ▶️️.

&amp; ⤴️ 👫 💪 🔄 🔄 🤔 👈 ⚫️ 🎲 🕳 🌖 🎏 `stanleyjobsox` 🌘 `johndoe`.

####  "🕴" 👊

↗️, 👊 🔜 🚫 🔄 🌐 👉 ✋, 👫 🔜 ✍ 📋 ⚫️, 🎲 ⏮️ 💯 ⚖️ 💯 💯 📍 🥈. &amp; 🔜 🤚 1️⃣ ➕ ☑ 🔤 🕰.

✋️ 🔨 👈, ⏲ ⚖️ 📆 👊 🔜 ✔️ 💭 ☑ 🆔 &amp; 🔐, ⏮️ "ℹ" 👆 🈸, ⚙️ 🕰 ✊ ❔.

#### 🔧 ⚫️ ⏮️ `secrets.compare_digest()`

✋️ 👆 📟 👥 🤙 ⚙️ `secrets.compare_digest()`.

📏, ⚫️ 🔜 ✊ 🎏 🕰 🔬 `stanleyjobsox` `stanleyjobson` 🌘 ⚫️ ✊ 🔬 `johndoe` `stanleyjobson`. &amp; 🎏 🔐.

👈 🌌, ⚙️ `secrets.compare_digest()` 👆 🈸 📟, ⚫️ 🔜 🔒 🛡 👉 🎂 ↔ 💂‍♂ 👊.

### 📨 ❌

⏮️ 🔍 👈 🎓 ❌, 📨 `HTTPException` ⏮️ 👔 📟 4️⃣0️⃣1️⃣ (🎏 📨 🕐❔ 🙅‍♂ 🎓 🚚) &amp; 🚮 🎚 `WWW-Authenticate` ⚒ 🖥 🎦 💳 📋 🔄:

{* ../../examples/security/tutorial007.py hl[23:27] *}
