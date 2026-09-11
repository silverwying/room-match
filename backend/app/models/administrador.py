from sqlalchemy import Column, Date, ForeignKey, Integer, String

from app.core.database import Base
from app.models.pessoa import Pessoa

class Administrador(Pessoa):
    __tablename__ = "administradores"

    id_administrador = Column(Integer, ForeignKey("pessoas.id_pessoa"), primary_key=True)
    nivel_acesso = Column(String(20), nullable=False)
    data_admissao = Column(Date, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "administrador"}
