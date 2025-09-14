"""
This example shows how to configure the HTTP client timeout for the MCP server.
In case you have API endpoints that take longer than 5 seconds to respond, you can increase the timeout.
"""

import httpx
from readyapi_mcp import ReadyApiMCP

from examples.shared.apps.items import app  # The ReadyAPI app
from examples.shared.setup import setup_logging

setup_logging()


mcp = ReadyApiMCP(app, http_client=httpx.AsyncClient(timeout=20))
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
