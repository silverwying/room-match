from pydantic import BaseModel, ConfigDict

class LocadorBase(BaseModel):
    cpf_cnpj: str

class LocadorCreate(LocadorBase):
    pass

class LocadorOut(LocadorBase):
    id_locador: int
    quantidade_imoveis_anunciados: int

    model_config = ConfigDict(from_attributes=True)
