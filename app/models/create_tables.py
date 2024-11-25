from app.core.database import Base, engine

if __name__ == "__main__":
    # Criar todas as tabelas no banco de dados
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
