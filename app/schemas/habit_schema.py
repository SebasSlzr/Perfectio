# /schemas/habit_schema.py

from datetime import date
from typing import Optional, List


# --- BASE/CREATE SCHEMAS ---
# Define los campos que se esperan al CREAR o actualizar un hábito.

# Nota: Si usas FastAPI/Pydantic, BaseModel debe importarse
# from pydantic import BaseModel
# Reemplaza 'object' con tu clase base de Schema si es necesario.

class HabitBase(object):
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

    # Aquí iría la configuración para que el objeto se pueda mapear
    # class Config:
    #    from_attributes = True