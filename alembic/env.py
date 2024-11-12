from logging.config import fileConfig
import os
from dotenv import load_dotenv

from sqlalchemy import engine_from_config, pool
from alembic import context

# Importe o Base que contém os metadados dos seus modelos
from app.db.base import Base  # Substitua pelo caminho correto para seus modelos

# make sure .env file is loaded containing database urls.
load_dotenv()

# Configuração do Alembic, leitura do .ini e URL do banco de dados
config = context.config
database_url = os.getenv("DATABASE_URL_AIVEN")
config.set_main_option("sqlalchemy.url", database_url)

# Configuração de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Defina target_metadata para incluir os metadados dos seus modelos
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa migrações no modo offline.

    Este modo configura o contexto com apenas uma URL,
    sem um objeto Engine. Não requer um DBAPI.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrações no modo online.

    Neste modo, criamos um Engine e associamos uma conexão com o contexto.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
