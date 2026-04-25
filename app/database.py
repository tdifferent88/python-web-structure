from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# cria conexão com banco SQLite (arquivo local)
engine = create_engine("sqlite:///site.db")

# cria sessões para acessar o banco
SessionLocal = sessionmaker(bind=engine)

# base para os modelos (tabelas)
Base = declarative_base()