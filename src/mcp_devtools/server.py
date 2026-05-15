"""MCP server entry point. Registers tools and runs the server."""

import logging
import sys
from mcp.server.fastmcp import FastMCP

# stdio mode requires logs to go to stderr, never stdout
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger("mcp_devtools")

# Create the MCP server instance
mcp = FastMCP()


@mcp.tool("ping", "A simple tool that returns 'pong'.")
def ping() -> str:
    """Health check tool that returns 'pong'. Use to verify the server is running."""
    logger.info("ping called")
    return "pong"


def main_stdio() -> None:
    """Run server in stdio mode (for Claude Desktop)."""
    mcp.run(transport="stdio")


def main_http() -> None:
    """Run server in streamable-http mode (for remote agents). Default port 8000."""
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    # Default to stdio so Claude Desktop can launch us directly
    main_stdio()
