from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Like(Base):
    __tablename__ = "likes"

    id_like = Column(Integer, primary_key=True, index=True)
    id_post = Column(Integer, ForeignKey("posts.id_post"), nullable=False)
    id_locatario = Column(Integer, ForeignKey("locatarios.id_locatario"), nullable=False)
    data_like = Column(DateTime, server_default=func.now())

    post = relationship("Post", backref="likes")
    locatario = relationship("Locatario", backref="likes")
