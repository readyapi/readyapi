import pytest
from readyapi.exceptions import ReadyAPIError

from ...utils import needs_py310


@needs_py310
def test_invalid_response_model():
    with pytest.raises(ReadyAPIError):
        from docs_src.response_model.tutorial003_04_py310 import app

        assert app  # pragma: no cover
