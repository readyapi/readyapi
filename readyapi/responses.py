from typing import Any, Dict, Optional

from starlette.responses import FileResponse as FileResponse  # noqa
from starlette.responses import HTMLResponse as HTMLResponse  # noqa
from starlette.responses import JSONResponse as JSONResponse  # noqa
from starlette.responses import PlainTextResponse as PlainTextResponse  # noqa
from starlette.responses import RedirectResponse as RedirectResponse  # noqa
from starlette.responses import Response as Response  # noqa
from starlette.responses import StreamingResponse as StreamingResponse  # noqa

try:
    import ujson
except ImportError:  # pragma: nocover
    ujson = None  # type: ignore


try:
    import orjson
except ImportError:  # pragma: nocover
    orjson = None  # type: ignore


class UJSONResponse(JSONResponse):
    """
    JSON response using the high-performance ujson library to serialize data to JSON.

    Read more about it in the
    [ReadyAPI docs for Custom Response - HTML, Stream, File, others](https://readyapi.khulnasoft.com/advanced/custom-response/).
    """

    def render(self, content: Any) -> bytes:
        assert ujson is not None, "ujson must be installed to use UJSONResponse"
        return ujson.dumps(content, ensure_ascii=False).encode("utf-8")


class ORJSONResponse(JSONResponse):
    """
    JSON response using the high-performance orjson library to serialize data to JSON.

    Read more about it in the
    [ReadyAPI docs for Custom Response - HTML, Stream, File, others](https://readyapi.khulnasoft.com/advanced/custom-response/).
    """

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(
            content, option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY
        )


class XMLResponse(Response):
    """
    XML response to serialize data to XML.

    Read more about it in the
    [ReadyAPI docs for Custom Response - HTML, Stream, File, others](https://readyapi.khulnasoft.com/advanced/custom-response/).
    """

    media_type = "application/xml"

    def render(self, content: Any) -> bytes:
        from xml.etree.ElementTree import Element, tostring

        def dict_to_xml(tag: str, d: Dict[str, Any]) -> Element:
            elem = Element(tag)
            for key, val in d.items():
                child = Element(key)
                child.text = str(val)
                elem.append(child)
            return elem

        root = dict_to_xml("root", content)
        return tostring(root)


class CustomResponse(Response):
    """
    Custom response to handle various content types.

    Read more about it in the
    [ReadyAPI docs for Custom Response - HTML, Stream, File, others](https://readyapi.khulnasoft.com/advanced/custom-response/).
    """

    def __init__(
        self,
        content: Any,
        status_code: int = 200,
        headers: Optional[Dict[str, str]] = None,
        media_type: Optional[str] = None,
        background: Optional[Any] = None,
    ) -> None:
        super().__init__(
            content=content,
            status_code=status_code,
            headers=headers,
            media_type=media_type,
            background=background,
        )

    def render(self, content: Any) -> bytes:
        if isinstance(content, dict):
            return JSONResponse(content).body
        elif isinstance(content, str):
            return PlainTextResponse(content).body
        elif isinstance(content, bytes):
            return content
        else:
            raise TypeError("Unsupported content type")
