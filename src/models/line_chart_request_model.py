from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, conlist
from .chart_series_model import Series

class LineChartRequest(BaseModel):
    title: Optional[str] = Field(None, description="Título do gráfico")
    x_label: Optional[str] = Field(None, description="Rótulo do eixo X")
    y_label: Optional[str] = Field(None, description="Rótulo do eixo Y")
    series: conlist(Series, min_length=1) = Field(..., description="Séries de dados")
    width: int = Field(900, description="Largura em pixels")
    height: int = Field(500, description="Altura em pixels")
    dpi: int = Field(100, description="DPI do gráfico")
    show_grid: bool = Field(True, description="Exibir grade")
    legend: bool = Field(True, description="Exibir legenda")
    format: str = Field("png", description="Formato da imagem de saída (ex: png, jpeg)")
