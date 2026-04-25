from app.database import Base, engine
from app.models import Projeto

# cria todas as tabelas no banco
Base.metadata.create_all(bind=engine)

print("Banco e tabelas criados com sucesso!")