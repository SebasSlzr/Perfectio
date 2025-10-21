# /schemas/habit_schema.py

from datetime import date
from typing import Optional, List
from pydantic import BaseModel



class HabitBase(BaseModel):
    """Estructura base del Hábito, utilizada para crear/actualizar."""
    title: str
    tag: str
    start_date: date
    frequency: str  # Ej: "diario", "lunes, miercoles, viernes"
    reminders: List[str]  # Lista de horarios, Ej: ["09:00", "18:30"]
    notes: Optional[str] = None  # Optional significa que es opcional
    color: str
    icon: str
    state: str = "activo"  # Estado por defecto al crear


class HabitCreate(HabitBase):
    """Schema para la creación de un nuevo Hábito."""
    # En este caso, hereda todos los campos de HabitBase.
    pass


# --- RESPONSE SCHEMA ---
# Define cómo se ve el Hábito cuando se lee (GET) desde la API.

class Habit(HabitBase):
    """Schema completo del Hábito, incluyendo el ID de la base de datos."""
    id_habit: int  # Se espera que la BD asigne este ID

