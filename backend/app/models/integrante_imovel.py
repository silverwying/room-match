from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class IntegranteImovel(Base):
    __tablename__ = "integrantes_imovel"

    id_integrante = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey("pessoas.id_pessoa"), nullable=False)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date, nullable=True)
    status_moradia = Column(String(20), default="ativo")

    pessoa = relationship("Pessoa")
    imovel = relationship("Imovel", backref="integrantes")
