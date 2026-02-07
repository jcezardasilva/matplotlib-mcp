from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Matplotlib Charts")

# Registrar tools
from services import timeline_chart_service  # noqa: E402,F401
from services import pie_chart_service  # noqa: E402,F401
