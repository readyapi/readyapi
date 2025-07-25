# 🔬

👏 <a href="https://www.starlette.io/testclient/" class="external-link" target="_blank">💃</a>, 🔬 **ReadyAPI** 🈸 ⏩ &amp; 😌.

⚫️ ⚓️ 🔛 <a href="https://www.python-httpx.org" class="external-link" target="_blank">🇸🇲</a>, ❔ 🔄 🏗 ⚓️ 🔛 📨, ⚫️ 📶 😰 &amp; 🏋️.

⏮️ ⚫️, 👆 💪 ⚙️ <a href="https://docs.pytest.org/" class="external-link" target="_blank">✳</a> 🔗 ⏮️ **ReadyAPI**.

## ⚙️ `TestClient`

/// info

⚙️ `TestClient`, 🥇 ❎ <a href="https://www.python-httpx.org" class="external-link" target="_blank">`httpx`</a>.

🤶 Ⓜ. `pip install httpx`.

///

🗄 `TestClient`.

✍ `TestClient` 🚶‍♀️ 👆 **ReadyAPI** 🈸 ⚫️.

✍ 🔢 ⏮️ 📛 👈 ▶️ ⏮️ `test_` (👉 🐩 `pytest` 🏛).

⚙️ `TestClient` 🎚 🎏 🌌 👆 ⏮️ `httpx`.

✍ 🙅 `assert` 📄 ⏮️ 🐩 🐍 🧬 👈 👆 💪 ✅ (🔄, 🐩 `pytest`).

{* ../../examples/app_testing/tutorial001.py hl[2,12,15:18] *}

/// tip

👀 👈 🔬 🔢 😐 `def`, 🚫 `async def`.

 &amp; 🤙 👩‍💻 😐 🤙, 🚫 ⚙️ `await`.

👉 ✔ 👆 ⚙️ `pytest` 🔗 🍵 🤢.

///

/// note | 📡 ℹ

👆 💪 ⚙️ `from starlette.testclient import TestClient`.

**ReadyAPI** 🚚 🎏 `starlette.testclient` `readyapi.testclient` 🏪 👆, 👩‍💻. ✋️ ⚫️ 👟 🔗 ⚪️➡️ 💃.

///

/// tip

🚥 👆 💚 🤙 `async` 🔢 👆 💯 ↖️ ⚪️➡️ 📨 📨 👆 ReadyAPI 🈸 (✅ 🔁 💽 🔢), ✔️ 👀 [🔁 💯](../advanced/async-tests.md){.internal-link target=_blank} 🏧 🔰.

///

## 🎏 💯

🎰 🈸, 👆 🎲 🔜 ✔️ 👆 💯 🎏 📁.

&amp; 👆 **ReadyAPI** 🈸 5️⃣📆 ✍ 📚 📁/🕹, ♒️.

### **ReadyAPI** 📱 📁

➡️ 💬 👆 ✔️ 📁 📊 🔬 [🦏 🈸](bigger-applications.md){.internal-link target=_blank}:

```
.
├── app
│   ├── __init__.py
│   └── main.py
```

📁 `main.py` 👆 ✔️ 👆 **ReadyAPI** 📱:


{* ../../examples/app_testing/main.py *}

### 🔬 📁

⤴️ 👆 💪 ✔️ 📁 `test_main.py` ⏮️ 👆 💯. ⚫️ 💪 🖖 🔛 🎏 🐍 📦 (🎏 📁 ⏮️ `__init__.py` 📁):

``` hl_lines="5"
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

↩️ 👉 📁 🎏 📦, 👆 💪 ⚙️ ⚖ 🗄 🗄 🎚 `app` ⚪️➡️ `main` 🕹 (`main.py`):

{* ../../examples/app_testing/test_main.py hl[3] *}

...&amp; ✔️ 📟 💯 💖 ⏭.

## 🔬: ↔ 🖼

🔜 ➡️ ↔ 👉 🖼 &amp; 🚮 🌖 ℹ 👀 ❔ 💯 🎏 🍕.

### ↔ **ReadyAPI** 📱 📁

➡️ 😣 ⏮️ 🎏 📁 📊 ⏭:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

➡️ 💬 👈 🔜 📁 `main.py` ⏮️ 👆 **ReadyAPI** 📱 ✔️ 🎏 **➡ 🛠️**.

⚫️ ✔️ `GET` 🛠️ 👈 💪 📨 ❌.

⚫️ ✔️ `POST` 🛠️ 👈 💪 📨 📚 ❌.

👯‍♂️ *➡ 🛠️* 🚚 `X-Token` 🎚.

{* ../../examples/app_testing/app_b/main.py *}

### ↔ 🔬 📁

👆 💪 ⤴️ ℹ `test_main.py` ⏮️ ↔ 💯:

{* ../../examples/app_testing/app_b/test_main.py *}

🕐❔ 👆 💪 👩‍💻 🚶‍♀️ ℹ 📨 &amp; 👆 🚫 💭 ❔, 👆 💪 🔎 (🇺🇸🔍) ❔ ⚫️ `httpx`, ⚖️ ❔ ⚫️ ⏮️ `requests`, 🇸🇲 🔧 ⚓️ 🔛 📨' 🔧.

⤴️ 👆 🎏 👆 💯.

🤶 Ⓜ.:

* 🚶‍♀️ *➡* ⚖️ *🔢* 🔢, 🚮 ⚫️ 📛 ⚫️.
* 🚶‍♀️ 🎻 💪, 🚶‍♀️ 🐍 🎚 (✅ `dict`) 🔢 `json`.
* 🚥 👆 💪 📨 *📨 💽* ↩️ 🎻, ⚙️ `data` 🔢 ↩️.
* 🚶‍♀️ *🎚*, ⚙️ `dict` `headers` 🔢.
*  *🍪*, `dict` `cookies` 🔢.

🌖 ℹ 🔃 ❔ 🚶‍♀️ 💽 👩‍💻 (⚙️ `httpx` ⚖️ `TestClient`) ✅ <a href="https://www.python-httpx.org" class="external-link" target="_blank">🇸🇲 🧾</a>.

/// info

🗒 👈 `TestClient` 📨 💽 👈 💪 🗜 🎻, 🚫 Pydantic 🏷.

🚥 👆 ✔️ Pydantic 🏷 👆 💯 &amp; 👆 💚 📨 🚮 💽 🈸 ⏮️ 🔬, 👆 💪 ⚙️ `jsonable_encoder` 🔬 [🎻 🔗 🔢](encoder.md){.internal-link target=_blank}.

///

## 🏃 ⚫️

⏮️ 👈, 👆 💪 ❎ `pytest`:

<div class="termy">

```console
$ pip install pytest

---> 100%
```

</div>

⚫️ 🔜 🔍 📁 &amp; 💯 🔁, 🛠️ 👫, &amp; 📄 🏁 🔙 👆.

🏃 💯 ⏮️:

<div class="termy">

```console
$ pytest

================ test session starts ================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/user/code/superawesome-cli/app
plugins: forked-1.1.3, xdist-1.31.0, cov-2.8.1
collected 6 items

---> 100%

test_main.py <span style="color: green; white-space: pre;">......                            [100%]</span>

<span style="color: green;">================= 1 passed in 0.03s =================</span>
```

</div>
