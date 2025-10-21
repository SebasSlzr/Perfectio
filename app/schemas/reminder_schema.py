from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ReminderBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    shouldRepeat: bool = False
    habit_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class ReminderCreate(ReminderBase):
    """Campos requeridos para crear un recordatorio (POST)."""
    pass
    model_config = ConfigDict(from_attributes=True)

class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    shouldRepeat: Optional[bool] = None
    habit_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class ReminderOut(ReminderBase):
    id_reminder: int
    model_config = ConfigDict(from_attributes=True)
