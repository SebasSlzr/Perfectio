from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from app.schemas.reminder import ReminderCreate, ReminderUpdate

router = APIRouter()

# GET /habits/{habit_id}/reminders
@router.get("/habits/{habit_id}/reminders")
async def list_reminders(
    habit_id: int = Path(..., description="ID del hábito asociado"),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    return {"msg": f"Listar recordatorios del hábito {habit_id} (skip={skip}, limit={limit})"}


# POST /habits/{habit_id}/reminders
@router.post("/habits/{habit_id}/reminders", response_model=ReminderCreate)
async def create_reminder(
    habit_id: int = Path(..., description="ID del hábito asociado"),
    db: AsyncSession = Depends(get_db)
):
    return {"msg": f"Recordatorio creado correctamente para el hábito {habit_id}"}


# PUT /reminders/{reminder_id}
@router.put("/reminders/{reminder_id}")
async def update_reminder(
    reminder_id: int = Path(..., description="ID del recordatorio a actualizar"),
    db: AsyncSession = Depends(get_db)
):
    return {"msg": f"Recordatorio {reminder_id} actualizado correctamente"}


# DELETE /reminders/{reminder_id}
@router.delete("/reminders/{reminder_id}")
async def delete_reminder(
    reminder_id: int = Path(..., description="ID del recordatorio a eliminar"),
    db: AsyncSession = Depends(get_db)
):
    return {"msg": f"Recordatorio {reminder_id} eliminado correctamente"}
