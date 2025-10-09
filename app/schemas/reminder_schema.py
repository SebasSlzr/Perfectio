from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReminderBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    shouldRepeat: bool = False

class ReminderCreate(ReminderBase):
    pass

class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    shouldRepeat: Optional[bool] = None

class ReminderResponse(ReminderBase):
    id: int
    habit_id: int

    class Config:
        orm_mode = True
