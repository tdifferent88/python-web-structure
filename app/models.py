from sqlalchemy import Column, Integer, String
from .database import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)