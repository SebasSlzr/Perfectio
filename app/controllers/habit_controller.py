# app/controllers/habit_controller.py
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.habits import Habit as HabitModel
from app.schemas.habit_schema import HabitCreate, HabitUpdate
from app.models.users import User as UserModel


async def _get_habit_or_404(habit_id: int, db: AsyncSession) -> HabitModel:
    result = await db.execute(select(HabitModel).where(HabitModel.id_habit == habit_id))
    habit = result.scalar_one_or_none()
    if not habit:
        raise HTTPException(status_code=404, detail="Habito no encontrado")
    return habit


async def _ensure_user_exists(user_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(UserModel).where(UserModel.id_user == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


async def get_all_habits(db: AsyncSession):
    """Devuelve todos los hábitos registrados."""
    result = await db.execute(select(HabitModel))
    habits = result.scalars().all()
    return habits


async def get_habit_by_id(habit_id: int, db: AsyncSession):
    """Obtiene un hábito específico."""
    return await _get_habit_or_404(habit_id, db)


async def create_habit(habit_data: HabitCreate, db: AsyncSession):
    """Crea un hábito validando la existencia del usuario dueño."""
    await _ensure_user_exists(habit_data.user_id, db)
    new_habit = HabitModel(**habit_data.model_dump())
    db.add(new_habit)
    await db.commit()
    await db.refresh(new_habit)
    return new_habit


async def update_habit(habit_id: int, habit_data: HabitUpdate, db: AsyncSession):
    """Actualiza los campos suministrados de un hábito."""
    habit = await _get_habit_or_404(habit_id, db)
    for key, value in habit_data.model_dump(exclude_unset=True).items():
        setattr(habit, key, value)

    await db.commit()
    await db.refresh(habit)
    return habit


async def delete_habit(habit_id: int, db: AsyncSession):
    """Elimina un hábito existente."""
    habit = await _get_habit_or_404(habit_id, db)

    await db.delete(habit)
    await db.commit()
    return {"detail": "Habito eliminado correctamente"}
