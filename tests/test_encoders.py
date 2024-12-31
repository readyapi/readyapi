import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional

import pytest
from pydantic import BaseModel
from readyapi.encoders import jsonable_encoder


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


def test_jsonable_encoder():
    item = Item(name="Foo", price=50.5, tax=10.5)
    encoded_item = jsonable_encoder(item)
    assert encoded_item == {
        "name": "Foo",
        "description": None,
        "price": 50.5,
        "tax": 10.5,
        "tags": [],
    }


def test_jsonable_encoder_with_enum():
    color = Color.RED
    encoded_color = jsonable_encoder(color)
    assert encoded_color == "red"


def test_jsonable_encoder_with_datetime():
    now = datetime.datetime.now()
    encoded_now = jsonable_encoder(now)
    assert encoded_now == now.isoformat()


def test_jsonable_encoder_with_decimal():
    value = Decimal("10.5")
    encoded_value = jsonable_encoder(value)
    assert encoded_value == 10.5


def test_jsonable_encoder_with_custom_encoder():
    def custom_encoder(value: Any) -> str:
        return f"custom-{value}"

    item = Item(name="Foo", price=50.5, tax=10.5)
    encoded_item = jsonable_encoder(item, custom_encoder={Item: custom_encoder})
    assert encoded_item == "custom-Item(name='Foo', description=None, price=50.5, tax=10.5, tags=[])"


def test_jsonable_encoder_with_include():
    item = Item(name="Foo", price=50.5, tax=10.5)
    encoded_item = jsonable_encoder(item, include={"name", "price"})
    assert encoded_item == {"name": "Foo", "price": 50.5}


def test_jsonable_encoder_with_exclude():
    item = Item(name="Foo", price=50.5, tax=10.5)
    encoded_item = jsonable_encoder(item, exclude={"tax"})
    assert encoded_item == {
        "name": "Foo",
        "description": None,
        "price": 50.5,
        "tags": [],
    }


def test_jsonable_encoder_with_exclude_none():
    item = Item(name="Foo", price=50.5, tax=None)
    encoded_item = jsonable_encoder(item, exclude_none=True)
    assert encoded_item == {"name": "Foo", "price": 50.5, "tags": []}


def test_jsonable_encoder_with_exclude_defaults():
    item = Item(name="Foo", price=50.5, tax=None)
    encoded_item = jsonable_encoder(item, exclude_defaults=True)
    assert encoded_item == {"name": "Foo", "price": 50.5}


def test_jsonable_encoder_with_exclude_unset():
    item = Item(name="Foo", price=50.5)
    encoded_item = jsonable_encoder(item, exclude_unset=True)
    assert encoded_item == {"name": "Foo", "price": 50.5, "tags": []}


def test_jsonable_encoder_with_sqlalchemy_safe():
    class SQLAlchemyItem:
        def __init__(self, name: str, price: float):
            self.name = name
            self.price = price
            self._sa_instance_state = "some state"

    item = SQLAlchemyItem(name="Foo", price=50.5)
    encoded_item = jsonable_encoder(item, sqlalchemy_safe=True)
    assert encoded_item == {"name": "Foo", "price": 50.5}
