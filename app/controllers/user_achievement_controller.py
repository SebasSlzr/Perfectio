from fastapi import HTTPException, status
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_achievement import UserAchievement
from app.models.users import User
from app.models.achievement import Achievement
from app.schemas.user_achievement_schemas import UserAchievementCreate


async def _ensure_user(user_id: int, db: AsyncSession):
    if await db.get(User, user_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


async def _ensure_achievement(achievement_id: int, db: AsyncSession):
    if await db.get(Achievement, achievement_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logro no encontrado")


async def assign_achievement(payload: UserAchievementCreate, db: AsyncSession):
    await _ensure_user(payload.user_id, db)
    await _ensure_achievement(payload.id_achievement, db)
    exists = await db.execute(
        select(UserAchievement).where(
            and_(
                UserAchievement.user_id == payload.user_id,
                UserAchievement.id_achievement == payload.id_achievement,
            )
        )
    )
    if exists.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya posee este logro",
        )
    record = UserAchievement(**payload.model_dump())
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record


async def get_user_achievements(user_id: int, db: AsyncSession):
    await _ensure_user(user_id, db)
    result = await db.execute(select(UserAchievement).where(UserAchievement.user_id == user_id))
    return result.scalars().all()


async def get_achievement_users(achievement_id: int, db: AsyncSession):
    await _ensure_achievement(achievement_id, db)
    result = await db.execute(
        select(UserAchievement).where(UserAchievement.id_achievement == achievement_id)
    )
    return result.scalars().all()
