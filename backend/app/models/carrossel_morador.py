from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class CarrosselMorador(Base):
    __tablename__ = "carrossel_moradores"

    id_carrossel_morador = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey("pessoas.id_pessoa"), nullable=False)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    url_imagem = Column(String(255), nullable=False)
    ordem_exibicao = Column(Integer, default=0)

    pessoa = relationship("Pessoa")
    imovel = relationship("Imovel", backref="carrossel_moradores")
