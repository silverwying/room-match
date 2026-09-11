from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AvaliacaoCreate(BaseModel):
    id_imovel: int
    nota: int = Field(ge=1, le=5)
    comentario: Optional[str] = None


class AvaliacaoOut(BaseModel):
    id_avaliacao: int
    id_imovel: int
    id_pessoa: int
    nota: int
    comentario: Optional[str] = None
    data_avaliacao: datetime

    model_config = ConfigDict(from_attributes=True)
