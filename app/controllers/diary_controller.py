from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.diary import Diary
from app.models.diary_entry import DiaryEntry
from app.models.users import User
from app.schemas.diary_schema import DiaryCreate, DiaryEntryCreate


async def _ensure_user_exists(user_id: int, db: AsyncSession):
    if await db.get(User, user_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


async def _get_diary_or_404(diary_id: int, db: AsyncSession) -> Diary:
    diary = await db.get(Diary, diary_id)
    if diary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diario no encontrado")
    return diary


async def get_diary_by_user(user_id: int, db: AsyncSession):
    result = await db.execute(select(Diary).where(Diary.user_id == user_id))
    diary = result.scalar_one_or_none()
    if diary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no tiene diario")
    return diary


async def create_diary(payload: DiaryCreate, db: AsyncSession):
    await _ensure_user_exists(payload.user_id, db)
    existing = await db.execute(select(Diary).where(Diary.user_id == payload.user_id))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya tiene un diario")
    diary = Diary(**payload.model_dump())
    db.add(diary)
    await db.commit()
    await db.refresh(diary)
    return diary


async def list_entries(diary_id: int, db: AsyncSession):
    await _get_diary_or_404(diary_id, db)
    result = await db.execute(select(DiaryEntry).where(DiaryEntry.diary_id == diary_id))
    return result.scalars().all()


async def create_entry(diary_id: int, payload: DiaryEntryCreate, db: AsyncSession):
    await _get_diary_or_404(diary_id, db)
    entry = DiaryEntry(diary_id=diary_id, **payload.model_dump())
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry
