from __future__ import annotations

from mcp.server.fastmcp import Image

from models.chart_request_model import BoxplotChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


@mcp.tool()
def render_boxplot_chart(request: BoxplotChartRequest) -> Image:
	"""Gera um boxplot e retorna no formato solicitado."""
	fig, ax = create_figure(request.width, request.height, request.dpi)

	ax.boxplot(request.values)
	if request.labels is not None:
		ax.set_xticks(list(range(1, len(request.labels) + 1)))
		ax.set_xticklabels(request.labels)

	if request.show_grid:
		ax.grid(True, axis="y", linestyle="--", alpha=0.4)

	apply_common_axes_settings(
		ax,
		title=request.title,
		x_label=request.x_label,
		y_label=request.y_label,
		legend=False,
	)
	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/boxplot", mime_type="application/json")
def example_boxplot_chart_request() -> dict:
	"""Exemplo de request para boxplot."""
	return {
		"title": "Distribuição por time",
		"x_label": "Time",
		"y_label": "Pontuação",
		"values": [
			[10, 12, 14, 18, 22],
			[8, 9, 11, 15, 19],
			[13, 15, 16, 20, 23],
		],
		"labels": ["A", "B", "C"],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"format": "png",
	}
