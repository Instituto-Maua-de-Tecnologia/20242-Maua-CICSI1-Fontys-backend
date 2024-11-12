from sqlalchemy.orm import Session
from app.db.base import create_tables
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import User

class UserRepository:
    def create_user(user: User) -> User:
        try: 
            db = get_db()
            new_user = User(
                user_id=user.user_id,
                email=user.email,
                name=user.name,
                password=user.password, 
            )
            db.add(new_user)
            db.commit()
            return new_user
        except Exception as e:
            print(e)
            raise e
        finally:
            db.close()
            

if __name__ == "__main__":
    # Teste a conexão e criação de tabelas
    try:
        create_tables()
        print("Conexão bem-sucedida e tabelas criadas.")
    except Exception as e:
        print(f"Erro ao conectar-se ao banco de dados: {e}")
