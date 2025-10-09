from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    progress: float = 0.0
    model_config = ConfigDict(from_attributes=True)
    
class GoalCreate(GoalBase):
    """Campos requeridos para crear una meta (POST)."""
    pass
    model_config = ConfigDict(from_attributes=True)

class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    progress: Optional[float] = None
    model_config = ConfigDict(from_attributes=True)
    
class GoalOut(GoalBase):
    id_goal: int
    model_config = ConfigDict(from_attributes=True)
    
    