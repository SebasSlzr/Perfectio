# app/routes/habit_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.habit_schema import Habit, HabitCreate, HabitUpdate
from app.controllers import habit_controller

router = APIRouter(
    prefix="/habits",
    tags=["Habits"],
    responses={404: {"description": "Hábito no encontrado"}},
)

@router.get(
    "/",
    response_model=list[Habit],
    summary="Listar hábitos",
    description="Obtiene todos los hábitos registrados para los usuarios.",
    response_description="Colección de hábitos.",
)
async def list_habits(db: AsyncSession = Depends(get_db)):
    return await habit_controller.get_all_habits(db)

@router.get(
    "/{habit_id}",
    response_model=Habit,
    summary="Obtener hábito",
    description="Devuelve la información de un hábito específico.",
    response_description="Datos del hábito solicitado.",
)
async def get_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return await habit_controller.get_habit_by_id(habit_id, db)

@router.post(
    "/",
    response_model=Habit,
    status_code=status.HTTP_201_CREATED,
    summary="Crear hábito",
    description="Registra un nuevo hábito ligado a un usuario.",
    response_description="Hábito creado correctamente.",
)
async def create_habit(habit: HabitCreate, db: AsyncSession = Depends(get_db)):
    return await habit_controller.create_habit(habit, db)

@router.put(
    "/{habit_id}",
    response_model=Habit,
    summary="Actualizar hábito",
    description="Modifica los detalles de un hábito existente.",
    response_description="Hábito actualizado.",
)
async def update_habit(habit_id: int, habit: HabitUpdate, db: AsyncSession = Depends(get_db)):
    return await habit_controller.update_habit(habit_id, habit, db)

@router.delete(
    "/{habit_id}",
    summary="Eliminar hábito",
    description="Borra el hábito especificado.",
    responses={200: {"description": "Hábito eliminado correctamente."}},
)
async def delete_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    return await habit_controller.delete_habit(habit_id, db)
