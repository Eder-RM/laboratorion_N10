# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# Estas funciones CRUD encapsulan la lógica de interacción con la base de datos.
# Son componentes reutilizables que pueden ser llamados desde cualquier endpoint.

def crear_evidencia(db: Session, evidencia: schemas.EvidenciaCreate):
    """
    Crea un nuevo registro de evidencia en la base de datos.
    """
    db_evidencia = models.Evidencia(**evidencia.model_dump())
    db.add(db_evidencia)
    db.commit()
    db.refresh(db_evidencia)
    return db_evidencia

def obtener_evidencias(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtiene una lista de evidencias de la base de datos con paginación.
    """
    return db.query(models.Evidencia).offset(skip).limit(limit).all()
