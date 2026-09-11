from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Post(Base):
    __tablename__ = "posts"

    id_post = Column(Integer, primary_key=True, index=True)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    id_locador = Column(Integer, ForeignKey("locadores.id_locador"), nullable=False)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text)
    data_publicacao = Column(DateTime(timezone=True), server_default=func.now())
    status_anuncio = Column(String(20), default="ativo")

    imovel = relationship("Imovel", backref="posts")
    locador = relationship("Locador", backref="posts")
