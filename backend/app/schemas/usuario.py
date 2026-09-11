from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    foto_perfil: Optional[str] = None
    bio: Optional[str] = None
    cidade_atual: Optional[str] = None
    tags_convivencia: Optional[List[str]] = None

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioOut(UsuarioBase):
    id_usuario: int
    data_cadastro: datetime
    status_verificacao: bool

    model_config = ConfigDict(from_attributes=True)
