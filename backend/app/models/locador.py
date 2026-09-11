from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Locador(Base):
    __tablename__ = "locadores"

    id_locador = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    cpf_cnpj = Column(String(20), unique=True, nullable=False)
    quantidade_imoveis_anunciados = Column(Integer, default=0)

    usuario = relationship("Usuario", backref="perfil_locador")
