import pytest


def test_main():
    with pytest.warns(DeprecationWarning):
        from examples.app_testing.tutorial003 import test_read_items
    test_read_items()
