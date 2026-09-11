from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Pessoa(Base):
    __tablename__ = "pessoas"

    id_pessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    tipo_pessoa = Column(String(20), nullable=False)

    # polymorphic_on faz o SQLAlchemy escolher Usuario ou Administrador
    # automaticamente ao ler uma linha de "pessoas", olhando tipo_pessoa.
    __mapper_args__ = {
        "polymorphic_identity": "pessoa",
        "polymorphic_on": tipo_pessoa,
    }
