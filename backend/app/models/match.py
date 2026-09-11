from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Match(Base):
    __tablename__ = "matches"

    id_match = Column(Integer, primary_key=True, index=True)
    id_locatario = Column(Integer, ForeignKey("locatarios.id_locatario"), nullable=False)
    id_post = Column(Integer, ForeignKey("posts.id_post"), nullable=False)
    percentual_afinidade = Column(Numeric(5, 2), nullable=False)
    tags_correspondentes = Column(ARRAY(String))
    data_calculo = Column(DateTime(timezone=True), server_default=func.now())

    locatario = relationship("Locatario", backref="matches")
    post = relationship("Post", backref="matches")
