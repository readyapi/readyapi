import pytest
from readyapi.exceptions import ReadyAPIError


def test_invalid_response_model():
    with pytest.raises(ReadyAPIError):
        from examples.response_model.tutorial003_04 import app

        assert app  # pragma: no cover
