from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from app.core.database import Base


class Visita(Base):
    __tablename__ = "visitas"

    id_visita = Column(Integer, primary_key=True, index=True)
    id_locatario = Column(Integer, ForeignKey("locatarios.id_locatario"), nullable=False)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    data_agendada = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    status_visita = Column(String(20), default="agendada")

    locatario = relationship("Locatario", backref="visitas")
    imovel = relationship("Imovel", backref="visitas")
