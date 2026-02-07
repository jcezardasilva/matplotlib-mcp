from __future__ import annotations

from typing import List

from mcp.server.fastmcp import Image

from models.chart_series_model import Series
from models.chart_request_model import ScatterChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


def _validate_series_lengths(series: List[Series]) -> None:
	for idx, s in enumerate(series):
		if s.x is not None and len(s.x) != len(s.y):
			raise ValueError(
				f"Série '{s.label}' (índice {idx}) possui tamanhos diferentes: x={len(s.x)} y={len(s.y)}"
			)


@mcp.tool()
def render_scatter_chart(request: ScatterChartRequest) -> Image:
	"""Gera um gráfico de dispersão e retorna no formato solicitado."""
	_validate_series_lengths(request.series)

	fig, ax = create_figure(request.width, request.height, request.dpi)

	for s in request.series:
		if s.x is None:
			x_vals = list(range(1, len(s.y) + 1))
		else:
			x_vals = s.x
		ax.scatter(x_vals, s.y, s=request.marker_size, alpha=request.alpha, label=s.label)

	if request.show_grid:
		ax.grid(True, linestyle="--", alpha=0.4)

	apply_common_axes_settings(
		ax,
		title=request.title,
		x_label=request.x_label,
		y_label=request.y_label,
		legend=request.legend,
	)
	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/scatter", mime_type="application/json")
def example_scatter_chart_request() -> dict:
	"""Exemplo de request para gráfico de dispersão."""
	return {
		"title": "Correlação",
		"x_label": "Variável X",
		"y_label": "Variável Y",
		"series": [
			{"label": "Grupo 1", "x": [1, 2, 3, 4], "y": [2.1, 2.9, 3.7, 4.2]},
			{"label": "Grupo 2", "x": [1, 2, 3, 4], "y": [1.2, 1.9, 2.6, 3.1]},
		],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"marker_size": 40,
		"alpha": 0.8,
		"format": "png",
	}
