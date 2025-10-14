from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from app.schemas.reminder import ReminderCreate, ReminderUpdate

router = APIRouter()

# GET /reminders/list
@router.get("/list")
async def list_reminders(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Listar recordatorios (skip={skip}, limit={limit})"}

# GET /reminders/{reminder_id}
@router.get("/{reminder_id}")
async def get_reminder(reminder_id: int = Path(..., description="ID del recordatorio"), db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del recordatorio {reminder_id}"}

# POST /reminders/
@router.post("/", response_model=ReminderCreate)
async def create_reminder(db: AsyncSession = Depends(get_db)):
    return {"msg": "Recordatorio creado correctamente"}

# PUT /reminders/{reminder_id}
@router.put("/{reminder_id}")
async def update_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Recordatorio {reminder_id} actualizado"}

# DELETE /reminders/{reminder_id}
@router.delete("/{reminder_id}")
async def delete_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Recordatorio {reminder_id} eliminado"}
