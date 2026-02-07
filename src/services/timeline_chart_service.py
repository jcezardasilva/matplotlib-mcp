from __future__ import annotations

import json
from typing import List

import matplotlib.pyplot as plt
from mcp.server.fastmcp import Image

from models.chart_series_model import Series
from models.chart_request_model import TimelineChartRequest
from services.chart_service import mcp
from services.chart_utils_service import (
	apply_common_axes_settings,
	create_figure,
	finalize_figure,
)


def _validate_series_lengths(series: List[Series]) -> None:
	for idx, s in enumerate(series):
		if s.x is not None and len(s.x) != len(s.y):
			raise ValueError(
				f"Série '{s.label}' (índice {idx}) possui tamanhos diferentes: x={len(s.x)} y={len(s.y)}"
			)


def _resolve_category_labels(series: List[Series]) -> List[str] | None:
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
def render_line_chart(request: TimelineChartRequest) -> Image:
	"""Gera um gráfico de linha com múltiplas séries e retorna no formato solicitado."""
	_validate_series_lengths(request.series)

	fig, ax = create_figure(request.width, request.height, request.dpi)

	for s in request.series:
		if s.x is None:
			x_vals = list(range(1, len(s.y) + 1))
		else:
			x_vals = s.x
		ax.plot(x_vals, s.y, label=s.label)

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


@mcp.tool()
def render_bar_chart(request: TimelineChartRequest) -> Image:
	"""Gera um gráfico de barras com múltiplas séries e retorna no formato solicitado."""
	_validate_series_lengths(request.series)
	labels = _resolve_category_labels(request.series)

	fig, ax = create_figure(request.width, request.height, request.dpi)

	count = len(request.series)
	bar_width = 0.8 / max(count, 1)
	x_positions = list(range(1, len(request.series[0].y) + 1))

	for idx, s in enumerate(request.series):
		offset = (idx - (count - 1) / 2) * bar_width
		ax.bar(
			[x + offset for x in x_positions],
			s.y,
			width=bar_width,
			label=s.label,
		)

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


@mcp.resource("examples://charts/line", mime_type="application/json")
def example_line_chart_request() -> object:
	"""Exemplo de request para gráfico de linha."""
	example = {
		"title": "Vendas por mês",
		"x_label": "Mês",
		"y_label": "Vendas",
		"series": [
			{"label": "Produto A", "y": [10, 20, 18, 25]},
			{"label": "Produto B", "x": [1, 2, 3, 4], "y": [8, 15, 22, 19]},
		],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"format": "png",
	}
	return example


@mcp.resource("examples://charts/bar", mime_type="application/json")
def example_bar_chart_request() -> object:
	"""Exemplo de request para gráfico de barras."""
	example = {
		"title": "Pedidos por categoria",
		"x_label": "Categoria",
		"y_label": "Qtd",
		"series": [
			{"label": "2024", "x": ["A", "B", "C"], "y": [12, 7, 15]},
			{"label": "2025", "x": ["A", "B", "C"], "y": [9, 11, 13]},
		],
		"width": 900,
		"height": 500,
		"dpi": 100,
		"show_grid": True,
		"legend": True,
		"format": "png",
	}
	return example
