from typing import Optional
from pydantic import BaseModel, ConfigDict

class ImovelBase(BaseModel):
    valor_aluguel: float
    valor_condominio: float = 0
    valor_iptu: float = 0
    valor_contas_extras: float = 0
    tipo_imovel: str
    quantidade_quartos: int
    vagas_disponiveis: int
    area_m2: Optional[float] = None
    descricao: Optional[str] = None

class ImovelCreate(ImovelBase):
    pass

class ImovelOut(ImovelBase):
    id_imovel: int
    status_disponibilidade: str

    model_config = ConfigDict(from_attributes=True)
