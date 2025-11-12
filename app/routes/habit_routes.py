# app/routes/habit_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.habit_schema import Habit, HabitCreate, HabitUpdate
from app.controllers import habit_controller

router = APIRouter(prefix="/habits", tags=["Habits"])

@router.get("/", response_model=list[Habit])
async def list_habits(db: AsyncSession = Depends(get_db)):
    return await habit_controller.get_all_habits(db)

@router.get("/{habit_id}", response_model=Habit)
async def get_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return await habit_controller.get_habit_by_id(habit_id, db)

@router.post("/", response_model=Habit)
async def create_habit(habit: HabitCreate, db: AsyncSession = Depends(get_db)):
    return await habit_controller.create_habit(habit, db)

@router.put("/{habit_id}", response_model=Habit)
async def update_habit(habit_id: int, habit: HabitUpdate, db: AsyncSession = Depends(get_db)):
    return await habit_controller.update_habit(habit_id, habit, db)

@router.delete("/{habit_id}")
async def delete_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return await habit_controller.delete_habit(habit_id, db)
