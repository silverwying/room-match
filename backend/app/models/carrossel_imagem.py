from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class CarrosselImagem(Base):
    __tablename__ = "carrossel_imagens"

    id_imagem = Column(Integer, primary_key=True, index=True)
    id_imovel = Column(Integer, ForeignKey("imoveis.id_imovel"), nullable=False)
    url_imagem = Column(String(255), nullable=False)
    ordem_exibicao = Column(Integer, default=0)

    imovel = relationship("Imovel", backref="imagens")
