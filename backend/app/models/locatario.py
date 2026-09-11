from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship

from app.core.database import Base


class Locatario(Base):
    __tablename__ = "locatarios"

    id_locatario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    orcamento_maximo = Column(Numeric(10, 2), nullable=False)
    tags_estilo_vida = Column(ARRAY(String))
    preferencias_moradia = Column(JSONB)
    raio_busca_km = Column(Numeric(5, 2))

    usuario = relationship("Usuario", backref="perfil_locatario")
