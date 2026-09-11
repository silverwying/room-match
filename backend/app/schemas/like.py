from datetime import datetime
from pydantic import BaseModel, ConfigDict

class LikeCreate(BaseModel):
    id_post: int

class LikeOut(BaseModel):
    id_like: int
    id_post: int
    id_locatario: int
    data_like: datetime

    model_config = ConfigDict(from_attributes=True)
