from __future__ import annotations

import json

from mcp.server.fastmcp import Image

from models.chart_request_model import PieChartRequest
from services.chart_service import mcp
from services.chart_utils_service import create_figure, finalize_figure


def _validate_pie_request(request: PieChartRequest) -> None:
	if len(request.labels) != len(request.values):
		raise ValueError("labels e values devem ter o mesmo tamanho.")


@mcp.tool()
def render_pie_chart(request: PieChartRequest) -> Image:
	"""Gera um gráfico de pizza e retorna no formato solicitado."""
	_validate_pie_request(request)
	fig, ax = create_figure(request.width, request.height, request.dpi)

	result = ax.pie(
		request.values,
		labels=None,
		startangle=request.start_angle,
		autopct="%1.1f%%",
	)
	wedges = result[0]

	if request.title:
		ax.set_title(request.title)

	if request.legend:
		ax.legend(wedges, request.labels, loc="center left", bbox_to_anchor=(1, 0.5))

	return finalize_figure(fig, request.format)


@mcp.tool()
def render_donut_chart(request: PieChartRequest) -> Image:
	"""Gera um gráfico de rosca e retorna no formato solicitado."""
	_validate_pie_request(request)
	fig, ax = create_figure(request.width, request.height, request.dpi)

	result = ax.pie(
		request.values,
		labels=None,
		startangle=request.start_angle,
		autopct="%1.1f%%",
		wedgeprops={"width": 0.35},
	)
	wedges = result[0]

	if request.title:
		ax.set_title(request.title)

	if request.legend:
		ax.legend(wedges, request.labels, loc="center left", bbox_to_anchor=(1, 0.5))

	return finalize_figure(fig, request.format)


@mcp.resource("examples://charts/pie", mime_type="application/json")
def example_pie_chart_request() -> object:
	"""Exemplo de request para gráfico de pizza."""
	example = {
		"title": "Participação por segmento",
		"labels": ["A", "B", "C"],
		"values": [35, 45, 20],
		"width": 700,
		"height": 700,
		"dpi": 100,
		"start_angle": 90,
		"legend": True,
		"format": "png",
	}
	return example


@mcp.resource("examples://charts/donut", mime_type="application/json")
def example_donut_chart_request() -> object:
	"""Exemplo de request para gráfico de rosca."""
	example = {
		"title": "Distribuição por canal",
		"labels": ["Web", "Mobile", "Loja"],
		"values": [55, 30, 15],
		"width": 700,
		"height": 700,
		"dpi": 100,
		"start_angle": 90,
		"legend": True,
		"format": "png",
	}
	return example
