from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PostBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class PostCreate(PostBase):
    id_imovel: int

class PostOut(PostBase):
    id_post: int
    id_imovel: int
    id_locador: int
    data_publicacao: datetime
    status_anuncio: str

    model_config = ConfigDict(from_attributes=True)
