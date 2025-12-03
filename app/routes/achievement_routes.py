# app/routes/achievement_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Achievement, AchievementCreate
from app.controllers import achievement_controller

router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"],
    responses={
        401: {"description": "No autorizado"},
        404: {"description": "Logro no encontrado"},
    },
)


@router.get(
    "/",
    response_model=list[Achievement],
    summary="Listar logros",
    description="Devuelve todos los logros disponibles en el sistema de gamificación.",
    response_description="Colección de logros registrados.",
)
async def list_achievements(db: AsyncSession = Depends(get_db)):
    """Lista los logros configurados."""
    return await achievement_controller.list_achievements(db)


@router.get(
    "/{achievement_id}",
    response_model=Achievement,
    summary="Obtener un logro",
    description="Recupera la información detallada de un logro concreto.",
    response_description="Información del logro solicitado.",
)
async def get_achievement(achievement_id: int, db: AsyncSession = Depends(get_db)):
    """Detalle de un logro específico."""
    return await achievement_controller.get_achievement(achievement_id, db)


@router.post(
    "/",
    response_model=Achievement,
    status_code=status.HTTP_201_CREATED,
    summary="Crear logro",
    description="Crea un nuevo logro con sus criterios y recompensas.",
    response_description="Logro creado correctamente.",
)
async def create_achievement(achievement: AchievementCreate, db: AsyncSession = Depends(get_db)):
    """Crea un nuevo logro en la plataforma."""
    return await achievement_controller.create_achievement(achievement, db)