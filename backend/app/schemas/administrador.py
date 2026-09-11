from datetime import date

from pydantic import BaseModel, ConfigDict


class AdministradorBase(BaseModel):
    nome: str
    nivel_acesso: str
    data_admissao: date


class AdministradorCreate(AdministradorBase):
    pass


class AdministradorOut(AdministradorBase):
    id_administrador: int

    model_config = ConfigDict(from_attributes=True)
