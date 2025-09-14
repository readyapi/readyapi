"""
This example shows how to re-register tools if you add endpoints after the MCP server was created.
"""

from readyapi_mcp import ReadyApiMCP

from examples.mcp.shared.apps.items import app  # The ReadyAPI app
from examples.mcp.shared.setup import setup_logging

setup_logging()

mcp = ReadyApiMCP(app)  # Add MCP server to the ReadyAPI app
mcp.mount_http()  # MCP server


# This endpoint will not be registered as a tool, since it was added after the MCP instance was created
@app.get("/new/endpoint/", operation_id="new_endpoint", response_model=dict[str, str])
async def new_endpoint():
    return {"message": "Hello, world!"}


# But if you re-run the setup, the new endpoints will now be exposed.
mcp.setup_server()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
