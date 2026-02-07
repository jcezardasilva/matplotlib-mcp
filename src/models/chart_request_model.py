from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from .chart_series_model import Series

class TimelineChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: list[Series] = Field(..., min_length=1, description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class PieChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    labels: list[str] = Field(..., min_length=1, description="Rótulos das fatias")
    values: list[float] = Field(..., min_length=1, description="Valores das fatias")
    width: int = Field(700, description="Largura em pixels")
    height: int = Field(700, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    start_angle: int = Field(90, description="Ângulo inicial")
    legend: bool = Field(True, description="Exibir legenda")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class ScatterChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: list[Series] = Field(..., min_length=1, description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    marker_size: int = Field(40, description="Tamanho dos marcadores")
    alpha: float = Field(0.8, description="Transparência dos pontos")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class AreaChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: list[Series] = Field(..., min_length=1, description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    fill_alpha: float = Field(0.3, description="Transparência do preenchimento")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class HistogramChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    values: list[float] = Field(..., min_length=1, description="Valores para o histograma")
    bins: int = Field(10, description="Número de bins")
    label: Optional[str] = Field(None, description="Rótulo da série")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(False, description="Exibir legenda")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class BoxplotChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    values: list[list[float]] = Field(..., min_length=1, description="Séries de valores")
    labels: Optional[list[str]] = Field(None, description="Rótulos das séries")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class HeatmapChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    values: list[list[float]] = Field(..., min_length=1, description="Matriz de valores")
    x_labels: Optional[list[str]] = Field(None, description="Rótulos do eixo X")
    y_labels: Optional[list[str]] = Field(None, description="Rótulos do eixo Y")
    cmap: str = Field("viridis", description="Mapa de cores")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class StackedBarChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: list[Series] = Field(..., min_length=1, description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")


class LineMarkersChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: list[Series] = Field(..., min_length=1, description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    marker: str = Field("o", description="Estilo do marcador")
    marker_size: int = Field(6, description="Tamanho do marcador")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")
