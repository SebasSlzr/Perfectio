# app/routes/achievement_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import Achievement, AchievementCreate

router = APIRouter()

@router.get("/", response_model=list[Achievement])
async def list_achievements(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todos los logros"}

@router.get("/{achievement_id}", response_model=Achievement)
async def get_achievement(achievement_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del logro {achievement_id}"}

@router.post("/", response_model=Achievement)
async def create_achievement(achievement: AchievementCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Logro creado correctamente"}