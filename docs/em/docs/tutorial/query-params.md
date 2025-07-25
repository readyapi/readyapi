# 🔢 🔢

🕐❔ 👆 📣 🎏 🔢 🔢 👈 🚫 🍕 ➡ 🔢, 👫 🔁 🔬 "🔢" 🔢.

{* ../../examples/query_params/tutorial001.py hl[9] *}

🔢 ⚒ 🔑-💲 👫 👈 🚶 ⏮️ `?` 📛, 🎏 `&` 🦹.

🖼, 📛:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

...🔢 🔢:

* `skip`: ⏮️ 💲 `0`
* `limit`: ⏮️ 💲 `10`

👫 🍕 📛, 👫 "🛎" 🎻.

✋️ 🕐❔ 👆 📣 👫 ⏮️ 🐍 🆎 (🖼 🔛, `int`), 👫 🗜 👈 🆎 &amp; ✔ 🛡 ⚫️.

🌐 🎏 🛠️ 👈 ⚖ ➡ 🔢 ✔ 🔢 🔢:

* 👨‍🎨 🐕‍🦺 (🎲)
* 💽 <abbr title="converting the string that comes from an HTTP request into Python data">"✍"</abbr>
* 💽 🔬
* 🏧 🧾

## 🔢

🔢 🔢 🚫 🔧 🍕 ➡, 👫 💪 📦 &amp; 💪 ✔️ 🔢 💲.

🖼 🔛 👫 ✔️ 🔢 💲 `skip=0` &amp; `limit=10`.

, 🔜 📛:

```
http://127.0.0.1:8000/items/
```

🔜 🎏 🔜:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

✋️ 🚥 👆 🚶, 🖼:

```
http://127.0.0.1:8000/items/?skip=20
```

🔢 💲 👆 🔢 🔜:

* `skip=20`: ↩️ 👆 ⚒ ⚫️ 📛
* `limit=10`: ↩️ 👈 🔢 💲

## 📦 🔢

🎏 🌌, 👆 💪 📣 📦 🔢 🔢, ⚒ 👫 🔢 `None`:

{* ../../examples/query_params/tutorial002.py hl[9] *}

👉 💼, 🔢 🔢 `q` 🔜 📦, &amp; 🔜 `None` 🔢.

/// check

👀 👈 **ReadyAPI** 🙃 🥃 👀 👈 ➡ 🔢 `item_id` ➡ 🔢 &amp; `q` 🚫,, ⚫️ 🔢 🔢.

///

## 🔢 🔢 🆎 🛠️

👆 💪 📣 `bool` 🆎, &amp; 👫 🔜 🗜:

{* ../../examples/query_params/tutorial003.py hl[9] *}

👉 💼, 🚥 👆 🚶:

```
http://127.0.0.1:8000/items/foo?short=1
```

⚖️

```
http://127.0.0.1:8000/items/foo?short=True
```

⚖️

```
http://127.0.0.1:8000/items/foo?short=true
```

⚖️

```
http://127.0.0.1:8000/items/foo?short=on
```

⚖️

```
http://127.0.0.1:8000/items/foo?short=yes
```

⚖️ 🙆 🎏 💼 📈 (🔠, 🥇 🔤 🔠, ♒️), 👆 🔢 🔜 👀 🔢 `short` ⏮️ `bool` 💲 `True`. ⏪ `False`.


## 💗 ➡ &amp; 🔢 🔢

👆 💪 📣 💗 ➡ 🔢 &amp; 🔢 🔢 🎏 🕰, **ReadyAPI** 💭 ❔ ❔.

&amp; 👆 🚫 ✔️ 📣 👫 🙆 🎯 ✔.

👫 🔜 🔬 📛:

{* ../../examples/query_params/tutorial004.py hl[8,10] *}

## ✔ 🔢 🔢

🕐❔ 👆 📣 🔢 💲 🚫-➡ 🔢 (🔜, 👥 ✔️ 🕴 👀 🔢 🔢), ⤴️ ⚫️ 🚫 ✔.

🚥 👆 🚫 💚 🚮 🎯 💲 ✋️ ⚒ ⚫️ 📦, ⚒ 🔢 `None`.

✋️ 🕐❔ 👆 💚 ⚒ 🔢 🔢 ✔, 👆 💪 🚫 📣 🙆 🔢 💲:

{* ../../examples/query_params/tutorial005.py hl[6:7] *}

📥 🔢 🔢 `needy` ✔ 🔢 🔢 🆎 `str`.

🚥 👆 📂 👆 🖥 📛 💖:

```
http://127.0.0.1:8000/items/foo-item
```

...🍵 ❎ ✔ 🔢 `needy`, 👆 🔜 👀 ❌ 💖:

```JSON
{
    "detail": [
        {
            "loc": [
                "query",
                "needy"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

`needy` 🚚 🔢, 👆 🔜 💪 ⚒ ⚫️ 📛:

```
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```

...👉 🔜 👷:

```JSON
{
    "item_id": "foo-item",
    "needy": "sooooneedy"
}
```

&amp; ↗️, 👆 💪 🔬 🔢 ✔, ✔️ 🔢 💲, &amp; 🍕 📦:

{* ../../examples/query_params/tutorial006.py hl[10] *}

👉 💼, 📤 3️⃣ 🔢 🔢:

* `needy`, ✔ `str`.
* `skip`, `int` ⏮️ 🔢 💲 `0`.
* `limit`, 📦 `int`.

/// tip

👆 💪 ⚙️ `Enum`Ⓜ 🎏 🌌 ⏮️ [➡ 🔢](path-params.md#_7){.internal-link target=_blank}.

///
