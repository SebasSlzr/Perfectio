# app/routes/reminder_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Reminder, ReminderCreate, ReminderUpdate

router = APIRouter()

@router.get("/", response_model=list[Reminder])
async def list_reminders(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todos los recordatorios"}

@router.get("/{reminder_id}", response_model=Reminder)
async def get_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del recordatorio {reminder_id}"}

@router.post("/", response_model=Reminder)
async def create_reminder(reminder: ReminderCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Recordatorio creado correctamente"}

@router.put("/{reminder_id}", response_model=Reminder)
async def update_reminder(reminder_id: int, reminder: ReminderUpdate, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Recordatorio {reminder_id} actualizado"}

@router.delete("/{reminder_id}")
async def delete_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Recordatorio {reminder_id} eliminado"}