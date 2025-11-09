# app/schemas/diary_schema.py
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class DiaryEntryBase(BaseModel):
    """Base para entrada de diario"""
    date: datetime
    content: str

class DiaryEntryCreate(DiaryEntryBase):
    """Crear entrada de diario"""
    diary_id: int

class DiaryEntry(DiaryEntryBase):
    """Entrada de diario completa"""
    id_entry: int
    diary_id: int

    class Config:
        from_attributes = True

class DiaryBase(BaseModel):
    """Base para diario"""
    pass

class DiaryCreate(DiaryBase):
    """Crear diario"""
    user_id: int

class Diary(DiaryBase):
    """Diario completo"""
    id_diary: int
    user_id: int
    entries: List[DiaryEntry] = []

    class Config:
        from_attributes = True