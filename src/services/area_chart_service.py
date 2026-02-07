from __future__ import annotations

from typing import List

from mcp.server.fastmcp import Image

from models.chart_series_model import Series
from models.chart_request_model import AreaChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


def _validate_series_lengths(series: List[Series]) -> None:
	for idx, s in enumerate(series):
		if s.x is not None and len(s.x) != len(s.y):
			raise ValueError(
				f"Série '{s.label}' (índice {idx}) possui tamanhos diferentes: x={len(s.x)} y={len(s.y)}"
			)


@mcp.tool()
def render_area_chart(request: AreaChartRequest) -> Image:
	"""Gera um gráfico de área e retorna no formato solicitado."""
	_validate_series_lengths(request.series)

	fig, ax = create_figure(request.width, request.height, request.dpi)

	for s in request.series:
		if s.x is None:
			x_vals = list(range(1, len(s.y) + 1))
		else:
			x_vals = s.x
		ax.plot(x_vals, s.y, label=s.label)
		ax.fill_between(x_vals, s.y, alpha=request.fill_alpha)

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


@mcp.resource("examples://charts/area", mime_type="application/json")
def example_area_chart_request() -> dict:
	"""Exemplo de request para gráfico de área."""
	return {
		"title": "Crescimento",
		"x_label": "Mês",
		"y_label": "Usuários",
		"series": [
			{"label": "Orgânico", "y": [100, 140, 180, 210]},
			{"label": "Pago", "y": [60, 80, 90, 120]},
		],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"fill_alpha": 0.3,
		"format": "png",
	}
