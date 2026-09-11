from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class Conversa(Base):
    __tablename__ = "conversas"

    id_conversa = Column(Integer, primary_key=True, index=True)
    id_locatario = Column(Integer, ForeignKey("locatarios.id_locatario"), nullable=False)
    id_post = Column(Integer, ForeignKey("posts.id_post"), nullable=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    status_conversa = Column(String(20), default="ativa")

    locatario = relationship("Locatario", backref="conversas") 
    post = relationship("Post", backref="conversas")
             