# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

# Estos esquemas Pydantic son reutilizables para validar datos de entrada
# y formatear datos de salida.

# Esquema base con los campos comunes.
class EvidenciaBase(BaseModel):
    descripcion: str
    tipo: str

# Esquema para la creación de una evidencia (hereda de Base).
class EvidenciaCreate(EvidenciaBase):
    pass

# Esquema para la lectura/salida de una evidencia (hereda de Base).
# Incluye campos que son generados por la base de datos (id, fecha).
class EvidenciaOut(EvidenciaBase):
    id: int
    fecha: datetime

    class Config:
        # Permite que Pydantic trabaje con modelos de SQLAlchemy.
        from_attributes = True
