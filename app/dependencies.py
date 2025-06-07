# app/dependencies.py
from .db import SessionLocal

# Esta es una dependencia de FastAPI reutilizable.
# Se encarga de crear una sesión de BD por cada petición y cerrarla al finalizar.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
