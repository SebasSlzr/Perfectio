# app/routes/user_achievement_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserAchievement, UserAchievementCreate

router = APIRouter()

@router.post("/", response_model=UserAchievement)
async def assign_achievement(assignment: UserAchievementCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Logro asignado al usuario correctamente"}

@router.get("/user/{user_id}/achievements")
async def get_user_achievements(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Logros del usuario {user_id}"}

@router.get("/achievement/{achievement_id}/users")
async def get_achievement_users(achievement_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Usuarios con el logro {achievement_id}"}