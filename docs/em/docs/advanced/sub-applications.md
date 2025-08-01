# 🎧 🈸 - 🗻

🚥 👆 💪 ✔️ 2️⃣ 🔬 ReadyAPI 🈸, ⏮️ 👫 👍 🔬 🗄 &amp; 👫 👍 🩺 ⚜, 👆 💪 ✔️ 👑 📱 &amp; "🗻" 1️⃣ (⚖️ 🌅) 🎧-🈸(Ⓜ).

## 🗜 **ReadyAPI** 🈸

"🗜" ⛓ ❎ 🍕 "🔬" 🈸 🎯 ➡, 👈 ⤴️ ✊ 💅 🚚 🌐 🔽 👈 ➡, ⏮️ _➡ 🛠️_ 📣 👈 🎧-🈸.

### 🔝-🎚 🈸

🥇, ✍ 👑, 🔝-🎚, **ReadyAPI** 🈸, &amp; 🚮 *➡ 🛠️*:

{* ../../examples/sub_applications/tutorial001.py hl[3,6:8] *}

### 🎧-🈸

⤴️, ✍ 👆 🎧-🈸, &amp; 🚮 *➡ 🛠️*.

👉 🎧-🈸 ➕1️⃣ 🐩 ReadyAPI 🈸, ✋️ 👉 1️⃣ 👈 🔜 "🗻":

{* ../../examples/sub_applications/tutorial001.py hl[11,14:16] *}

### 🗻 🎧-🈸

👆 🔝-🎚 🈸, `app`, 🗻 🎧-🈸, `subapi`.

👉 💼, ⚫️ 🔜 📌 ➡ `/subapi`:

{* ../../examples/sub_applications/tutorial001.py hl[11,19] *}

### ✅ 🏧 🛠️ 🩺

🔜, 🏃 `uvicorn` ⏮️ 👑 📱, 🚥 👆 📁 `main.py`, ⚫️ 🔜:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

&amp; 📂 🩺 <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

👆 🔜 👀 🏧 🛠️ 🩺 👑 📱, 🔌 🕴 🚮 👍 _➡ 🛠️_:

<img src="/img/tutorial/sub-applications/image01.png">

&amp; ⤴️, 📂 🩺 🎧-🈸, <a href="http://127.0.0.1:8000/subapi/docs" class="external-link" target="_blank">http://127.0.0.1:8000/subapi/docs</a>.

👆 🔜 👀 🏧 🛠️ 🩺 🎧-🈸, ✅ 🕴 🚮 👍 _➡ 🛠️_, 🌐 🔽 ☑ 🎧-➡ 🔡 `/subapi`:

<img src="/img/tutorial/sub-applications/image02.png">

🚥 👆 🔄 🔗 ⏮️ 🙆 2️⃣ 👩‍💻 🔢, 👫 🔜 👷 ☑, ↩️ 🖥 🔜 💪 💬 🔠 🎯 📱 ⚖️ 🎧-📱.

### 📡 ℹ: `root_path`

🕐❔ 👆 🗻 🎧-🈸 🔬 🔛, ReadyAPI 🔜 ✊ 💅 🔗 🗻 ➡ 🎧-🈸 ⚙️ 🛠️ ⚪️➡️ 🔫 🔧 🤙 `root_path`.

👈 🌌, 🎧-🈸 🔜 💭 ⚙️ 👈 ➡ 🔡 🩺 🎚.

&amp; 🎧-🈸 💪 ✔️ 🚮 👍 📌 🎧-🈸 &amp; 🌐 🔜 👷 ☑, ↩️ ReadyAPI 🍵 🌐 👉 `root_path`Ⓜ 🔁.

👆 🔜 💡 🌅 🔃 `root_path` &amp; ❔ ⚙️ ⚫️ 🎯 📄 🔃 [⛅ 🗳](behind-a-proxy.md){.internal-link target=_blank}.
