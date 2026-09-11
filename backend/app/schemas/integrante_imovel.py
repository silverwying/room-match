from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class IntegranteImovelBase(BaseModel):
    id_pessoa: int
    id_imovel: int
    data_entrada: date


class IntegranteImovelCreate(IntegranteImovelBase):
    pass


class IntegranteImovelOut(IntegranteImovelBase):
    id_integrante: int
    data_saida: Optional[date] = None
    status_moradia: str

    model_config = ConfigDict(from_attributes=True)
