from __future__ import annotations

from mcp.server.fastmcp import Image

from models.chart_request_model import HistogramChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


@mcp.tool()
def render_histogram_chart(request: HistogramChartRequest) -> Image:
	"""Gera um histograma e retorna no formato solicitado."""
	fig, ax = create_figure(request.width, request.height, request.dpi)

	ax.hist(request.values, bins=request.bins, alpha=0.75, label=request.label)

	if request.show_grid:
		ax.grid(True, axis="y", linestyle="--", alpha=0.4)

	apply_common_axes_settings(
		ax,
		title=request.title,
		x_label=request.x_label,
		y_label=request.y_label,
		legend=request.legend and request.label is not None,
	)
	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/histogram", mime_type="application/json")
def example_histogram_chart_request() -> dict:
	"""Exemplo de request para histograma."""
	return {
		"title": "Distribuição de idades",
		"x_label": "Idade",
		"y_label": "Frequência",
		"values": [18, 21, 22, 23, 25, 29, 30, 31, 35, 40, 41, 45],
		"bins": 6,
		"label": "Idades",
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"format": "png",
	}
