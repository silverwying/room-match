from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MensagemCreate(BaseModel):
    conteudo: str


class MensagemOut(BaseModel):
    id_mensagem: int
    id_conversa: int
    id_remetente: int
    conteudo: str
    data_envio: datetime
    status_leitura: bool

    model_config = ConfigDict(from_attributes=True)
