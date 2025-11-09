# app/schemas/goal_habit_schemas.py
from pydantic import BaseModel
from typing import List

class GoalHabitBase(BaseModel):
    """Base para relacion meta-habito"""
    id_goal: int
    id_habit: int

class GoalHabitCreate(GoalHabitBase):
    """Crear relacion meta-habito"""
    pass

class GoalHabit(GoalHabitBase):
    """Relacion meta-habito completa"""

    class Config:
        from_attributes = True