# app/schemas/user_achievement_schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserAchievementBase(BaseModel):
    """Base para relacion usuario-logro"""
    user_id: int
    id_achievement: int
    date_achieved: datetime

class UserAchievementCreate(UserAchievementBase):
    """Crear relacion usuario-logro"""
    pass

class UserAchievement(UserAchievementBase):
    """Relacion usuario-logro completa"""

    class Config:
        from_attributes = True