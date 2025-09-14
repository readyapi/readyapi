"""
This example shows how to mount the MCP server to a specific APIRouter, giving a custom mount path.
"""

from examples.shared.apps.items import app  # The ReadyAPI app
from examples.shared.setup import setup_logging

from readyapi import APIRouter
from readyapi_mcp import ReadyApiMCP

setup_logging()

other_router = APIRouter(prefix="/other/route")
app.include_router(other_router)

mcp = ReadyApiMCP(app)

# Mount the MCP server to a specific router.
# It will now only be available at `/other/route/mcp`
mcp.mount_http(other_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
