from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict

class LocatarioBase(BaseModel):
    orcamento_maximo: float
    tags_estilo_vida: Optional[List[str]] = None
    preferencias_moradia: Optional[Dict[str, Any]] = None
    raio_busca_km: Optional[float] = None

class LocatarioCreate(LocatarioBase):
    pass

class LocatarioOut(LocatarioBase):
    id_locatario: int

    model_config = ConfigDict(from_attributes=True)
