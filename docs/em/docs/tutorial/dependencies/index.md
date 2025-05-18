# 🔗

**ReadyAPI** ✔️ 📶 🏋️ ✋️ 🏋️ **<abbr title="also known as components, resources, providers, services, injectables">🔗 💉</abbr>** ⚙️.

⚫️ 🏗 📶 🙅 ⚙️, &amp; ⚒ ⚫️ 📶 ⏩ 🙆 👩‍💻 🛠️ 🎏 🦲 ⏮️ **ReadyAPI**.

## ⚫️❔ "🔗 💉"

**"🔗 💉"** ⛓, 📋, 👈 📤 🌌 👆 📟 (👉 💼, 👆 *➡ 🛠️ 🔢*) 📣 👜 👈 ⚫️ 🚚 👷 &amp; ⚙️: "🔗".

&amp; ⤴️, 👈 ⚙️ (👉 💼 **ReadyAPI**) 🔜 ✊ 💅 🔨 ⚫️❔ 💪 🚚 👆 📟 ⏮️ 📚 💪 🔗 ("💉" 🔗).

👉 📶 ⚠ 🕐❔ 👆 💪:

* ✔️ 💰 ⚛ (🎏 📟 ⚛ 🔄 &amp; 🔄).
* 💰 💽 🔗.
* 🛠️ 💂‍♂, 🤝, 🔑 📄, ♒️.
*  &amp; 📚 🎏 👜...

🌐 👫, ⏪ 📉 📟 🔁.

## 🥇 🔁

➡️ 👀 📶 🙅 🖼. ⚫️ 🔜 🙅 👈 ⚫️ 🚫 📶 ⚠, 🔜.

✋️ 👉 🌌 👥 💪 🎯 🔛 ❔ **🔗 💉** ⚙️ 👷.

### ✍ 🔗, ⚖️ "☑"

➡️ 🥇 🎯 🔛 🔗.

⚫️ 🔢 👈 💪 ✊ 🌐 🎏 🔢 👈 *➡ 🛠️ 🔢* 💪 ✊:

{* ../../docs_src/dependencies/tutorial001.py hl[8:11] *}

👈 ⚫️.

**2️⃣ ⏸**.

&amp; ⚫️ ✔️ 🎏 💠 &amp; 📊 👈 🌐 👆 *➡ 🛠️ 🔢* ✔️.

👆 💪 💭 ⚫️ *➡ 🛠️ 🔢* 🍵 "👨‍🎨" (🍵 `@app.get("/some-path")`).

&amp; ⚫️ 💪 📨 🕳 👆 💚.

👉 💼, 👉 🔗 ⌛:

* 📦 🔢 🔢 `q` 👈 `str`.
* 📦 🔢 🔢 `skip` 👈 `int`, &amp; 🔢 `0`.
* 📦 🔢 🔢 `limit` 👈 `int`, &amp; 🔢 `100`.

&amp; ⤴️ ⚫️ 📨 `dict` ⚗ 📚 💲.

### 🗄 `Depends`

{* ../../docs_src/dependencies/tutorial001.py hl[3] *}

### 📣 🔗, "⚓️"

🎏 🌌 👆 ⚙️ `Body`, `Query`, ♒️. ⏮️ 👆 *➡ 🛠️ 🔢* 🔢, ⚙️ `Depends` ⏮️ 🆕 🔢:

{* ../../docs_src/dependencies/tutorial001.py hl[15,20] *}

👐 👆 ⚙️ `Depends` 🔢 👆 🔢 🎏 🌌 👆 ⚙️ `Body`, `Query`, ♒️, `Depends` 👷 👄 🎏.

👆 🕴 🤝 `Depends` 👁 🔢.

👉 🔢 🔜 🕳 💖 🔢.

&amp; 👈 🔢 ✊ 🔢 🎏 🌌 👈 *➡ 🛠️ 🔢* .

/// tip

👆 🔜 👀 ⚫️❔ 🎏 "👜", ↖️ ⚪️➡️ 🔢, 💪 ⚙️ 🔗 ⏭ 📃.

///

🕐❔ 🆕 📨 🛬, **ReadyAPI** 🔜 ✊ 💅:

* 🤙 👆 🔗 ("☑") 🔢 ⏮️ ☑ 🔢.
* 🤚 🏁 ⚪️➡️ 👆 🔢.
* 🛠️ 👈 🏁 🔢 👆 *➡ 🛠️ 🔢*.

```mermaid
graph TB

common_parameters(["common_parameters"])
read_items["/items/"]
read_users["/users/"]

common_parameters --> read_items
common_parameters --> read_users
```

👉 🌌 👆 ✍ 🔗 📟 🕐 &amp; **ReadyAPI** ✊ 💅 🤙 ⚫️ 👆 *➡ 🛠️*.

/// check

👀 👈 👆 🚫 ✔️ ✍ 🎁 🎓 &amp; 🚶‍♀️ ⚫️ 👱 **ReadyAPI** "®" ⚫️ ⚖️ 🕳 🎏.

👆 🚶‍♀️ ⚫️ `Depends` &amp; **ReadyAPI** 💭 ❔ 🎂.

///

##  `async` ⚖️ 🚫 `async`

🔗 🔜 🤙 **ReadyAPI** (🎏 👆 *➡ 🛠️ 🔢*), 🎏 🚫 ✔ ⏪ 🔬 👆 🔢.

👆 💪 ⚙️ `async def` ⚖️ 😐 `def`.

&amp; 👆 💪 📣 🔗 ⏮️ `async def` 🔘 😐 `def` *➡ 🛠️ 🔢*, ⚖️ `def` 🔗 🔘 `async def` *➡ 🛠️ 🔢*, ♒️.

⚫️ 🚫 🤔. **ReadyAPI** 🔜 💭 ⚫️❔.

/// note

🚥 👆 🚫 💭, ✅ [🔁: *"🏃 ❓" *](../../async.md){.internal-link target=_blank} 📄 🔃 `async` &amp; `await` 🩺.

///

## 🛠️ ⏮️ 🗄

🌐 📨 📄, 🔬 &amp; 📄 👆 🔗 (&amp; 🎧-🔗) 🔜 🛠️ 🎏 🗄 🔗.

, 🎓 🩺 🔜 ✔️ 🌐 ℹ ⚪️➡️ 👫 🔗 💁‍♂️:

<img src="/img/tutorial/dependencies/image01.png">

## 🙅 ⚙️

🚥 👆 👀 ⚫️, *➡ 🛠️ 🔢* 📣 ⚙️ 🕐❔ *➡* &amp; *🛠️* 🏏, &amp; ⤴️ **ReadyAPI** ✊ 💅 🤙 🔢 ⏮️ ☑ 🔢, ❎ 📊 ⚪️➡️ 📨.

🤙, 🌐 (⚖️ 🏆) 🕸 🛠️ 👷 👉 🎏 🌌.

👆 🙅 🤙 👈 🔢 🔗. 👫 🤙 👆 🛠️ (👉 💼, **ReadyAPI**).

⏮️ 🔗 💉 ⚙️, 👆 💪 💬 **ReadyAPI** 👈 👆 *➡ 🛠️ 🔢* "🪀" 🔛 🕳 🙆 👈 🔜 🛠️ ⏭ 👆 *➡ 🛠️ 🔢*, &amp; **ReadyAPI** 🔜 ✊ 💅 🛠️ ⚫️ &amp; "💉" 🏁.

🎏 ⚠ ⚖ 👉 🎏 💭 "🔗 💉":

* ℹ
* 🐕‍🦺
* 🐕‍🦺
* 💉
* 🦲

## **ReadyAPI** 🔌-🔌

🛠️ &amp; "🔌-"Ⓜ 💪 🏗 ⚙️ **🔗 💉** ⚙️. ✋️ 👐, 📤 🤙 **🙅‍♂ 💪 ✍ "🔌-🔌"**, ⚙️ 🔗 ⚫️ 💪 📣 ♾ 🔢 🛠️ &amp; 🔗 👈 ▶️️ 💪 👆 *➡ 🛠️ 🔢*.

&amp; 🔗 💪 ✍ 📶 🙅 &amp; 🏋️ 🌌 👈 ✔ 👆 🗄 🐍 📦 👆 💪, &amp; 🛠️ 👫 ⏮️ 👆 🛠️ 🔢 👩‍❤‍👨 ⏸ 📟, *🌖*.

👆 🔜 👀 🖼 👉 ⏭ 📃, 🔃 🔗 &amp; ☁ 💽, 💂‍♂, ♒️.

## **ReadyAPI** 🔗

🦁 🔗 💉 ⚙️ ⚒ **ReadyAPI** 🔗 ⏮️:

* 🌐 🔗 💽
* ☁ 💽
* 🔢 📦
* 🔢 🔗
* 🤝 &amp; ✔ ⚙️
* 🛠️ ⚙️ ⚖ ⚙️
* 📨 💽 💉 ⚙️
* ♒️.

## 🙅 &amp; 🏋️

👐 🔗 🔗 💉 ⚙️ 📶 🙅 🔬 &amp; ⚙️, ⚫️ 📶 🏋️.

👆 💪 🔬 🔗 👈 🔄 💪 🔬 🔗 👫.

🔚, 🔗 🌲 🔗 🏗, &amp; **🔗 💉** ⚙️ ✊ 💅 🔬 🌐 👉 🔗 👆 (&amp; 👫 🎧-🔗) &amp; 🚚 (💉) 🏁 🔠 🔁.

🖼, ➡️ 💬 👆 ✔️ 4️⃣ 🛠️ 🔗 (*➡ 🛠️*):

* `/items/public/`
* `/items/private/`
* `/users/{user_id}/activate`
* `/items/pro/`

⤴️ 👆 💪 🚮 🎏 ✔ 📄 🔠 👫 ⏮️ 🔗 &amp; 🎧-🔗:

```mermaid
graph TB

current_user(["current_user"])
active_user(["active_user"])
admin_user(["admin_user"])
paying_user(["paying_user"])

public["/items/public/"]
private["/items/private/"]
activate_user["/users/{user_id}/activate"]
pro_items["/items/pro/"]

current_user --> active_user
active_user --> admin_user
active_user --> paying_user

current_user --> public
active_user --> private
admin_user --> activate_user
paying_user --> pro_items
```

## 🛠️ ⏮️ **🗄**

🌐 👫 🔗, ⏪ 📣 👫 📄, 🚮 🔢, 🔬, ♒️. 👆 *➡ 🛠️*.

**ReadyAPI** 🔜 ✊ 💅 🚮 ⚫️ 🌐 🗄 🔗, 👈 ⚫️ 🎦 🎓 🧾 ⚙️.
