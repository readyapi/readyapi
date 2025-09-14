"""
This example shows how to describe the full response schema instead of just a response example.
"""

from examples.shared.apps.items import app  # The ReadyAPI app
from examples.shared.setup import setup_logging

from readyapi_mcp import ReadyApiMCP

setup_logging()

# Add MCP server to the ReadyAPI app
mcp = ReadyApiMCP(
    app,
    name="Item API MCP",
    description="MCP server for the Item API",
    describe_full_response_schema=True,  # Describe the full response JSON-schema instead of just a response example
    describe_all_responses=True,  # Describe all the possible responses instead of just the success (2XX) response
)

mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
