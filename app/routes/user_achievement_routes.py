# app/routes/user_achievement_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserAchievement, UserAchievementCreate
from app.controllers import user_achievement_controller

router = APIRouter(
    prefix="/user-achievements",
    tags=["User-Achievements"],
    responses={404: {"description": "Asignación no encontrada"}},
)


@router.post(
    "/",
    response_model=UserAchievement,
    status_code=status.HTTP_201_CREATED,
    summary="Asignar logro a usuario",
    description="Vincula un logro existente a un usuario.",
    response_description="Logro asignado correctamente.",
)
async def assign_achievement(assignment: UserAchievementCreate, db: AsyncSession = Depends(get_db)):
    """Asigna un logro a un usuario."""
    return await user_achievement_controller.assign_achievement(assignment, db)


@router.get(
    "/user/{user_id}/achievements",
    response_model=list[UserAchievement],
    summary="Listar logros por usuario",
    description="Obtiene todos los logros que posee el usuario.",
    responses={200: {"description": "Listado de logros del usuario."}},
)
async def get_user_achievements(user_id: int, db: AsyncSession = Depends(get_db)):
    """Lista los logros de un usuario."""
    return await user_achievement_controller.get_user_achievements(user_id, db)


@router.get(
    "/achievement/{achievement_id}/users",
    response_model=list[UserAchievement],
    summary="Listar usuarios por logro",
    description="Devuelve los usuarios que han conseguido el logro especificado.",
    responses={200: {"description": "Listado de usuarios con el logro."}},
)
async def get_achievement_users(achievement_id: int, db: AsyncSession = Depends(get_db)):
    """Lista usuarios que poseen un logro."""
    return await user_achievement_controller.get_achievement_users(achievement_id, db)