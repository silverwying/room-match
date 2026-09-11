from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConversaCreate(BaseModel):
    id_post: int


class ConversaOut(BaseModel):
    id_conversa: int
    id_locatario: int
    id_post: int
    data_criacao: datetime
    status_conversa: str

    model_config = ConfigDict(from_attributes=True)
