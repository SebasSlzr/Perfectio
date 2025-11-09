# app/schemas/achievement_schema.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AchievementBase(BaseModel):
    """Estructura base de un logro"""
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    points_awarded: int = 0

class AchievementCreate(AchievementBase):
    """Schema para crear un logro"""
    pass

class Achievement(AchievementBase):
    """Schema completo del logro"""
    id_achievement: int

    class Config:
        from_attributes = True