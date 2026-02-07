from __future__ import annotations

from mcp.server.fastmcp import Image

from models.chart_request_model import HeatmapChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


@mcp.tool()
def render_heatmap_chart(request: HeatmapChartRequest) -> Image:
	"""Gera um heatmap e retorna no formato solicitado."""
	fig, ax = create_figure(request.width, request.height, request.dpi)

	im = ax.imshow(request.values, cmap=request.cmap, aspect="auto")
	fig.colorbar(im, ax=ax)

	if request.x_labels is not None:
		ax.set_xticks(list(range(len(request.x_labels))))
		ax.set_xticklabels(request.x_labels)
	if request.y_labels is not None:
		ax.set_yticks(list(range(len(request.y_labels))))
		ax.set_yticklabels(request.y_labels)

	apply_common_axes_settings(
		ax,
		title=request.title,
		x_label=request.x_label,
		y_label=request.y_label,
		legend=False,
	)
	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/heatmap", mime_type="application/json")
def example_heatmap_chart_request() -> dict:
	"""Exemplo de request para heatmap."""
	return {
		"title": "Matriz de intensidade",
		"x_label": "Dia",
		"y_label": "Hora",
		"values": [
			[1, 2, 3, 4],
			[2, 3, 4, 5],
			[3, 4, 5, 6],
		],
		"x_labels": ["Seg", "Ter", "Qua", "Qui"],
		"y_labels": ["Manhã", "Tarde", "Noite"],
		"cmap": "viridis",
		"width": 900,
		"height": 500,
		"dpi": 100,
		"format": "png",
	}
