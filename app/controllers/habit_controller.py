# app/controllers/habit_controller.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.habits import Habit as HabitModel
from app.schemas.habit_schema import HabitCreate, HabitUpdate


async def get_all_habits(db: AsyncSession):
    result = await db.execute(select(HabitModel))
    habits = result.scalars().all()
    return habits


async def get_habit_by_id(habit_id: int, db: AsyncSession):
    result = await db.execute(select(HabitModel).where(HabitModel.id_habit == habit_id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=404, detail="Habito no encontrado")
    return habit


async def create_habit(habit_data: HabitCreate, db: AsyncSession):
    new_habit = HabitModel(**habit_data.dict())
    db.add(new_habit)
    await db.commit()
    await db.refresh(new_habit)
    return new_habit


async def update_habit(habit_id: int, habit_data: HabitUpdate, db: AsyncSession):
    result = await db.execute(select(HabitModel).where(HabitModel.id_habit == habit_id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=404, detail="Habito no encontrado")

    for key, value in habit_data.dict(exclude_unset=True).items():
        setattr(habit, key, value)

    await db.commit()
    await db.refresh(habit)
    return habit


async def delete_habit(habit_id: int, db: AsyncSession):
    result = await db.execute(select(HabitModel).where(HabitModel.id_habit == habit_id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=404, detail="Habito no encontrado")

    await db.delete(habit)
    await db.commit()
    return {"detail": "Habito eliminado correctamente"}
