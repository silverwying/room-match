from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class RotaMobilidade(Base):
    __tablename__ = "rotas_mobilidade"

    id_rota = Column(Integer, primary_key=True, index=True)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    destino = Column(String(150), nullable=False)
    meio_transporte = Column(String(30), nullable=False)
    distancia_km = Column(Numeric(6, 2))
    tempo_estimado_min = Column(Integer)

    imovel = relationship("Imovel", backref="rotas_mobilidade")
