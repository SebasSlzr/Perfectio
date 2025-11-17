from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class GoalBase(BaseModel):
    """
    Base schema for Goal, used for shared fields.
    """
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    progress: float = 0.0
    model_config = ConfigDict(from_attributes=True)

class GoalCreate(GoalBase):
    """
    Schema for creating a new Goal (POST).
    Inherits all fields from GoalBase.
    """
    pass
    model_config = ConfigDict(from_attributes=True)

class GoalUpdate(BaseModel):
    """
    Schema for updating an existing Goal (PATCH/PUT).
    All fields are optional.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    progress: Optional[float] = None
    model_config = ConfigDict(from_attributes=True)

class Goal(GoalBase):
    """
    Schema for returning Goal data in responses.
    """
    id_goal: int
    model_config = ConfigDict(from_attributes=True)

