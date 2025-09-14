from examples.shared.apps.items import app  # The ReadyAPI app
from examples.shared.setup import setup_logging

from readyapi_mcp import ReadyApiMCP

setup_logging()

# Add MCP server to the ReadyAPI app
mcp = ReadyApiMCP(app)

# Mount the MCP server to the ReadyAPI app
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
