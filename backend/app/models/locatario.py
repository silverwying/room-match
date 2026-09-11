from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Locatario(Base):
    __tablename__ = "locatarios"

    # Extensão 1:1 opcional de Usuario (não é herança polimórfica): um usuário
    # só ganha uma linha aqui se decidir buscar moradia. Pode ter também uma
    # linha em locadores ao mesmo tempo.
    id_locatario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    orcamento_maximo = Column(Numeric(10, 2), nullable=False)
    tags_estilo_vida = Column(Text)
    preferencias_moradia = Column(Text)
    raio_busca_km = Column(Numeric(5, 2))

    usuario = relationship("Usuario", backref="perfil_locatario")
