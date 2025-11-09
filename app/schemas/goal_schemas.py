# app/schemas/goal_schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class GoalBase(BaseModel):
    """Base para meta"""
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    progress: float = 0.0

class GoalCreate(GoalBase):
    """Crear meta"""
    user_id: int

class GoalUpdate(BaseModel):
    """Actualizar meta"""
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    progress: Optional[float] = None

class Goal(GoalBase):
    """Meta completa"""
    id_goal: int
    user_id: int

    class Config:
        from_attributes = True