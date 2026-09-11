from typing import Optional

from pydantic import BaseModel, ConfigDict


class EnderecoImovelBase(BaseModel):
    rua: str
    numero: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class EnderecoImovelCreate(EnderecoImovelBase):
    id_imovel: int


class EnderecoImovelOut(EnderecoImovelBase):
    id_endereco: int
    id_imovel: int

    model_config = ConfigDict(from_attributes=True)
