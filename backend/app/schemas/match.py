from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MatchOut(BaseModel):
    id_match: int
    id_locatario: int
    id_post: int
    percentual_afinidade: float
    tags_correspondentes: Optional[str] = None
    data_calculo: datetime

    model_config = ConfigDict(from_attributes=True)
