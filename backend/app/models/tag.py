from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Tag(Base):
    __tablename__ = "tags"

    id_tag = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
    categoria = Column(String(30))
