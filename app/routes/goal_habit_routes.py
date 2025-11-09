# app/routes/goal_habit_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import GoalHabit, GoalHabitCreate

router = APIRouter()

@router.post("/", response_model=GoalHabit)
async def associate_goal_habit(association: GoalHabitCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Hábito asociado a meta correctamente"}

@router.delete("/{goal_id}/{habit_id}")
async def remove_goal_habit_association(goal_id: int, habit_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Asociación meta {goal_id} - hábito {habit_id} eliminada"}