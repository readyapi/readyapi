"""
This example shows how to run the MCP server and the ReadyAPI app separately.
You can create an MCP server from one ReadyAPI app, and mount it to a different app.
"""

from readyapi import ReadyAPI
from readyapi_mcp import ReadyApiMCP

from examples.shared.apps.items import app
from examples.shared.setup import setup_logging

setup_logging()

MCP_SERVER_HOST = "localhost"
MCP_SERVER_PORT = 8000
ITEMS_API_HOST = "localhost"
ITEMS_API_PORT = 8001


# Take the ReadyAPI app only as a source for MCP server generation
mcp = ReadyApiMCP(app)

# Mount the MCP server to a separate ReadyAPI app
mcp_app = ReadyAPI()
mcp.mount_http(mcp_app)

# Run the MCP server separately from the original ReadyAPI app.
# It still works 🚀
# Your original API is **not exposed**, only via the MCP server.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(mcp_app, host="0.0.0.0", port=8000)
