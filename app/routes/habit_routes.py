# app/routes/habit_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import Habit, HabitCreate, HabitUpdate

router = APIRouter()

@router.get("/", response_model=list[Habit])
async def list_habits(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todos los hábitos"}

@router.get("/{habit_id}", response_model=Habit)
async def get_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del hábito {habit_id}"}

@router.post("/", response_model=Habit)
async def create_habit(habit: HabitCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Hábito creado correctamente"}

@router.put("/{habit_id}", response_model=Habit)
async def update_habit(habit_id: int, habit: HabitUpdate, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Hábito {habit_id} actualizado"}

@router.delete("/{habit_id}")
async def delete_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Hábito {habit_id} eliminado"}

@router.get("/{habit_id}/reminders")
async def get_habit_reminders(habit_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Recordatorios del hábito {habit_id}"}