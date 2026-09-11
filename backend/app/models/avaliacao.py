from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id_avaliacao = Column(Integer, primary_key=True, index=True)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    id_pessoa = Column(Integer, ForeignKey("pessoas.id_pessoa"), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(Text)
    data_avaliacao = Column(DateTime(timezone=True), server_default=func.now())

    imovel = relationship("Imovel", backref="avaliacoes")
    pessoa = relationship("Pessoa")
