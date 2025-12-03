from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.reminder import Reminder as ReminderModel
from app.models.habits import Habit as HabitModel
from app.schemas.reminder_schema import ReminderCreate, ReminderUpdate

async def _get_reminder_or_404(reminder_id: int, db: AsyncSession) -> ReminderModel:
    """Obtiene un recordatorio específico o lanza un 404."""
    reminder = await db.get(ReminderModel, reminder_id)
    if reminder is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recordatorio con ID {reminder_id} no encontrado.",
        )
    return reminder

async def _ensure_habit_exists(habit_id: int, db: AsyncSession) -> None:
    if await db.get(HabitModel, habit_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habito no encontrado",
        )

async def get_all_reminders(db: AsyncSession):
    """Lista todos los recordatorios."""
    result = await db.execute(select(ReminderModel))
    return result.scalars().all()

async def get_reminder_by_id(reminder_id: int, db: AsyncSession):
    """Obtiene un recordatorio específico."""
    return await _get_reminder_or_404(reminder_id, db)

async def get_reminders_by_habit(habit_id: int, db: AsyncSession):
    """Devuelve los recordatorios asociados a un hábito."""
    result = await db.execute(select(ReminderModel).where(ReminderModel.habit_id == habit_id))
    return result.scalars().all()

async def create_reminder(reminder_data: ReminderCreate, db: AsyncSession):
    """Crea y persiste un nuevo recordatorio."""
    await _ensure_habit_exists(reminder_data.habit_id, db)
    reminder = ReminderModel(**reminder_data.model_dump())
    db.add(reminder)
    await db.commit()
    await db.refresh(reminder)
    return reminder

async def update_reminder(reminder_id: int, reminder_data: ReminderUpdate, db: AsyncSession):
    """Actualiza parcialmente un recordatorio."""
    reminder = await _get_reminder_or_404(reminder_id, db)
    for key, value in reminder_data.model_dump(exclude_unset=True).items():
        setattr(reminder, key, value)
    await db.commit()
    await db.refresh(reminder)
    return reminder

async def delete_reminder(reminder_id: int, db: AsyncSession):
    """Elimina un recordatorio existente."""
    reminder = await _get_reminder_or_404(reminder_id, db)
    await db.delete(reminder)
    await db.commit()
    return {"detail": f"Recordatorio {reminder_id} eliminado"}
