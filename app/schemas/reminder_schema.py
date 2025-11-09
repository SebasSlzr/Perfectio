# app/schemas/reminder_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReminderBase(BaseModel):
    """Base para recordatorio"""
    title: str
    description: Optional[str] = None
    date: datetime
    shouldRepeat: bool = False

class ReminderCreate(ReminderBase):
    """Crear recordatorio"""
    habit_id: int

class ReminderUpdate(BaseModel):
    """Actualizar recordatorio"""
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    shouldRepeat: Optional[bool] = None

class Reminder(ReminderBase):
    """Recordatorio completo"""
    id_reminder: int
    habit_id: int

    class Config:
        from_attributes = True