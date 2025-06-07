# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

# It's a good practice to be explicit with relative imports
from . import crud, models, schemas
from .db import engine
from .dependencies import get_db

# Create database tables
# This will create the tables defined in your models.py file
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestión de Evidencias Forenses",
    description="API para gestionar la cadena de custodia de evidencias forenses.",
    version="1.0.0"
)

@app.post("/evidencias/", response_model=schemas.EvidenciaOut, tags=["Evidencias"])
def crear_evidencia(evidencia: schemas.EvidenciaCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva evidencia en la base de datos.
    """
    return crud.crear_evidencia(db, evidencia)

@app.get("/evidencias/", response_model=List[schemas.EvidenciaOut], tags=["Evidencias"])
def obtener_evidencias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de evidencias de la base de datos.
    """
    evidencias = crud.obtener_evidencias(db, skip=skip, limit=limit)
    return evidencias

