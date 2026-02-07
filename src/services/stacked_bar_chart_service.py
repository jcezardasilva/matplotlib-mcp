from __future__ import annotations

from typing import List

from mcp.server.fastmcp import Image

from models.chart_series_model import Series
from models.chart_request_model import StackedBarChartRequest
from services.chart_service import mcp
from services.chart_utils_service import apply_common_axes_settings, create_figure, finalize_figure


def _validate_series_lengths(series: List[Series]) -> None:
	for idx, s in enumerate(series):
		if s.x is not None and len(s.x) != len(s.y):
			raise ValueError(
				f"Série '{s.label}' (índice {idx}) possui tamanhos diferentes: x={len(s.x)} y={len(s.y)}"
			)


def _resolve_category_labels(series: List[Series]) -> list[str] | None:
	if not series or series[0].x is None:
		return None
	labels = [str(v) for v in series[0].x]
	for s in series[1:]:
		if s.x is None:
			continue
		if [str(v) for v in s.x] != labels:
			raise ValueError("Todas as séries com x precisam compartilhar os mesmos rótulos.")
	return labels


@mcp.tool()
def render_stacked_bar_chart(request: StackedBarChartRequest) -> Image:
	"""Gera um gráfico de barras empilhadas e retorna no formato solicitado."""
	_validate_series_lengths(request.series)
	labels = _resolve_category_labels(request.series)

	fig, ax = create_figure(request.width, request.height, request.dpi)

	x_positions = list(range(1, len(request.series[0].y) + 1))
	bottom = [0.0 for _ in x_positions]

	for s in request.series:
		ax.bar(x_positions, s.y, bottom=bottom, label=s.label)
		bottom = [b + v for b, v in zip(bottom, s.y)]

	if labels is not None:
		ax.set_xticks(x_positions)
		ax.set_xticklabels(labels)

	if request.show_grid:
		ax.grid(True, axis="y", linestyle="--", alpha=0.4)

	apply_common_axes_settings(
		ax,
		title=request.title,
		x_label=request.x_label,
		y_label=request.y_label,
		legend=request.legend,
	)
	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/stacked-bar", mime_type="application/json")
def example_stacked_bar_chart_request() -> dict:
	"""Exemplo de request para barras empilhadas."""
	return {
		"title": "Composição por categoria",
		"x_label": "Categoria",
		"y_label": "Qtd",
		"series": [
			{"label": "Online", "x": [1, 2, 3], "y": [4, 6, 5]},
			{"label": "Loja", "x": [1, 2, 3], "y": [3, 2, 4]},
			{"label": "Parceiros", "x": [1, 2, 3], "y": [2, 3, 1]},
		],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"format": "png",
	}
