# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexión a la base de datos SQLite (un archivo local)
# Este es nuestro producto COTS integrado.
DATABASE_URL = "sqlite:///./evidencias.db"

# El argumento check_same_thread es necesario solo para SQLite.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cada instancia de SessionLocal será una sesión de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para que nuestros modelos de SQLAlchemy hereden de ella.
Base = declarative_base()
