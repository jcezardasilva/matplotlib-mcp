from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Matplotlib Charts")

# Registrar tools
from services import timeline_chart_service  # noqa: E402,F401
from services import pie_chart_service  # noqa: E402,F401
from services import scatter_chart_service  # noqa: E402,F401
from services import area_chart_service  # noqa: E402,F401
from services import histogram_chart_service  # noqa: E402,F401
from services import boxplot_chart_service  # noqa: E402,F401
from services import heatmap_chart_service  # noqa: E402,F401
from services import stacked_bar_chart_service  # noqa: E402,F401
from services import line_markers_chart_service  # noqa: E402,F401
