# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from .db import Base
import datetime

# Modelo SQLAlchemy para la tabla 'evidencias'
# Esta clase es un componente reutilizable que define la estructura de datos en la BD.
class Evidencia(Base):
    __tablename__ = "evidencias"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    tipo = Column(String, index=True)
    fecha = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
