# /schemas/achievement_schema.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# --- BASE SCHEMA ---
class AchievementBase(BaseModel):
    """Estructura base de un logro, usada para crear o actualizar."""
    title: str
    description: Optional[str] = None
    date: datetime
    user_id: int  # Clave foránea hacia el usuario


# --- CREATE SCHEMA ---
class AchievementCreate(AchievementBase):
    """Schema para creación de logros."""
    pass


# --- RESPONSE SCHEMA ---
class Achievement(AchievementBase):
    """Schema completo del logro, incluyendo su ID y emblema relacionado."""
    id_achievement: int
    emblem: Optional[str] = None  # Podría ser el nombre del emblema si se relaciona

    class Config:
        from_attributes = True  # Permite convertir desde modelos ORM
