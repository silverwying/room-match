from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Mensagem(Base):
    __tablename__ = "mensagens"

    id_mensagem = Column(Integer, primary_key=True, index=True)
    id_conversa = Column(Integer, ForeignKey("conversas.id_conversa"), nullable=False)
    id_remetente = Column(Integer, ForeignKey("pessoas.id_pessoa"), nullable=False)
    conteudo = Column(Text, nullable=False)
    data_envio = Column(DateTime(timezone=True), server_default=func.now())
    status_leitura = Column(Boolean, default=False)

    conversa = relationship("Conversa", backref="mensagens")
    remetente = relationship("Pessoa")
