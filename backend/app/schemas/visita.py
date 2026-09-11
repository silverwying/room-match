from datetime import date, time
from pydantic import BaseModel, ConfigDict

class VisitaCreate(BaseModel):
    id_imovel: int
    data_agendada: date
    horario: time

class VisitaOut(BaseModel):
    id_visita: int
    id_locatario: int
    id_imovel: int
    data_agendada: date
    horario: time
    status_visita: str

    model_config = ConfigDict(from_attributes=True)
