from __future__ import annotations

import io
from typing import List

import matplotlib
import matplotlib.pyplot as plt
from mcp.server.fastmcp import FastMCP, Image

from models.chart_series_model import Series
from models.line_chart_request_model import LineChartRequest

matplotlib.use("Agg")

mcp = FastMCP("Matplotlib Charts")

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

def _create_figure(request: LineChartRequest):
    width_in = request.width / request.dpi
    height_in = request.height / request.dpi
    return plt.subplots(figsize=(width_in, height_in), dpi=request.dpi)

def _apply_common_axes_settings(ax, request: LineChartRequest) -> None:
    if request.title:
        ax.set_title(request.title)
    if request.x_label:
        ax.set_xlabel(request.x_label)
    if request.y_label:
        ax.set_ylabel(request.y_label)

    if request.legend:
        ax.legend()

def _finalize_figure(fig, request: LineChartRequest) -> Image:
    fig.tight_layout()
    buffer = io.BytesIO()
    fig.savefig(buffer, format=request.format)
    plt.close(fig)
    return Image(data=buffer.getvalue(), format=request.format)

@mcp.tool()
def render_line_chart(request: LineChartRequest) -> Image:
    """Gera um gráfico de linha com múltiplas séries e retorna no formato solicitado."""
    _validate_series_lengths(request.series)

    fig, ax = _create_figure(request)

    for s in request.series:
        if s.x is None:
            x_vals = list(range(1, len(s.y) + 1))
        else:
            x_vals = s.x
        ax.plot(x_vals, s.y, label=s.label)

    if request.show_grid:
        ax.grid(True, linestyle="--", alpha=0.4)

    _apply_common_axes_settings(ax, request)
    return _finalize_figure(fig, request)

@mcp.tool()
def render_bar_chart(request: LineChartRequest) -> Image:
    """Gera um gráfico de barras com múltiplas séries e retorna no formato solicitado."""
    _validate_series_lengths(request.series)
    labels = _resolve_category_labels(request.series)

    fig, ax = _create_figure(request)

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

    _apply_common_axes_settings(ax, request)
    return _finalize_figure(fig, request)
