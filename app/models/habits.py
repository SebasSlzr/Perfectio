# /schemas/habit_schema.py

from datetime import date
from typing import Optional, List
from pydantic import BaseModel  # 👈 IMPORTANTE


class HabitBase(BaseModel):  # 👈 Debe heredar de BaseModel
    """Estructura base del Hábito, utilizada para crear/actualizar."""
    title: str
    tag: str
    start_date: date
    frequency: str  # Ej: "diario", "lunes, miercoles, viernes"
    reminders: List[str]  # Lista de horarios, Ej: ["09:00", "18:30"]
    notes: Optional[str] = None
    color: str
    icon: str
    state: str = "activo"  # Estado por defecto al crear


class HabitCreate(HabitBase):
    """Schema para la creación de un nuevo Hábito."""
    pass


class Habit(HabitBase):
    """Schema completo del Hábito, incluyendo el ID de la base de datos."""
    id_habit: int
