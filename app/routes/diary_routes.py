# app/routes/diary_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Diary, DiaryCreate, DiaryEntry, DiaryEntryCreate

router = APIRouter()

@router.get("/{user_id}", response_model=Diary)
async def get_diary(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Diario del usuario {user_id}"}

@router.post("/", response_model=Diary)
async def create_diary(diary: DiaryCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Diario creado correctamente"}

@router.get("/{diary_id}/entries", response_model=list[DiaryEntry])
async def list_diary_entries(diary_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Entradas del diario {diary_id}"}

@router.post("/{diary_id}/entries", response_model=DiaryEntry)
async def create_diary_entry(diary_id: int, entry: DiaryEntryCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Entrada creada en el diario {diary_id}"}