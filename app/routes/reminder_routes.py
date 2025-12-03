# app/routes/reminder_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Reminder, ReminderCreate, ReminderUpdate
from app.controllers import reminders_controller

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"],
    responses={404: {"description": "Recordatorio no encontrado"}},
)


@router.get(
    "/",
    response_model=list[Reminder],
    summary="Listar recordatorios",
    description="Devuelve todos los recordatorios configurados.",
    response_description="Colección de recordatorios.",
)
async def list_reminders(db: AsyncSession = Depends(get_db)):
    """Lista recordatorios."""
    return await reminders_controller.get_all_reminders(db)


@router.get(
    "/{reminder_id}",
    response_model=Reminder,
    summary="Obtener recordatorio",
    description="Devuelve la información de un recordatorio específico.",
    response_description="Detalles del recordatorio.",
)
async def get_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    """Obtiene un recordatorio específico."""
    return await reminders_controller.get_reminder_by_id(reminder_id, db)


@router.post(
    "/",
    response_model=Reminder,
    status_code=status.HTTP_201_CREATED,
    summary="Crear recordatorio",
    description="Registra un nuevo recordatorio ligado a una meta o hábito.",
    response_description="Recordatorio creado correctamente.",
)
async def create_reminder(reminder: ReminderCreate, db: AsyncSession = Depends(get_db)):
    """Crea un nuevo recordatorio."""
    return await reminders_controller.create_reminder(reminder, db)


@router.put(
    "/{reminder_id}",
    response_model=Reminder,
    summary="Actualizar recordatorio",
    description="Modifica los atributos de un recordatorio.",
    response_description="Recordatorio actualizado.",
)
async def update_reminder(reminder_id: int, reminder: ReminderUpdate, db: AsyncSession = Depends(get_db)):
    """Actualiza un recordatorio existente."""
    return await reminders_controller.update_reminder(reminder_id, reminder, db)


@router.delete(
    "/{reminder_id}",
    summary="Eliminar recordatorio",
    description="Elimina el recordatorio indicado.",
    responses={200: {"description": "Recordatorio eliminado correctamente."}},
)
async def delete_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    """Elimina un recordatorio."""
    return await reminders_controller.delete_reminder(reminder_id, db)