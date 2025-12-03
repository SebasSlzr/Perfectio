from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.achievement import Achievement
from app.schemas.achievement_schema import AchievementCreate


async def _get_achievement_or_404(achievement_id: int, db: AsyncSession) -> Achievement:
    achievement = await db.get(Achievement, achievement_id)
    if achievement is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logro no encontrado")
    return achievement


async def list_achievements(db: AsyncSession):
    result = await db.execute(select(Achievement))
    return result.scalars().all()


async def get_achievement(achievement_id: int, db: AsyncSession):
    return await _get_achievement_or_404(achievement_id, db)


async def create_achievement(payload: AchievementCreate, db: AsyncSession):
    achievement = Achievement(**payload.model_dump())
    db.add(achievement)
    await db.commit()
    await db.refresh(achievement)
    return achievement
