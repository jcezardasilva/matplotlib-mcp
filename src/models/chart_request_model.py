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
