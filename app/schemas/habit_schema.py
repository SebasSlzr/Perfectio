# app/schemas/habit_schema.py
from datetime import date
from typing import Optional
from pydantic import BaseModel

class HabitBase(BaseModel):
    """Base para habito"""
    title: str
    tag: str
    start_date: date
    frequency: str
    color: str
    icon: str
    state: str = "activo"

class HabitCreate(HabitBase):
    """Crear habito"""
    user_id: int

class HabitUpdate(BaseModel):
    """Actualizar habito"""
    title: Optional[str] = None
    tag: Optional[str] = None
    frequency: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    state: Optional[str] = None

class Habit(HabitBase):
    """Habito completo"""
    id_habit: int
    user_id: int

    class Config:
        from_attributes = True