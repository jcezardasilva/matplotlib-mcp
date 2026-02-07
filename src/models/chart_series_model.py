from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, conlist

class Series(BaseModel):
    label: str = Field(..., description="Nome da série")
    y: conlist(float, min_length=1) = Field(..., description="Valores no eixo Y")
    x: Optional[conlist(float, min_length=1)] = Field(
        None,
        description="Valores no eixo X (opcional; se ausente usa índice)",
    )
