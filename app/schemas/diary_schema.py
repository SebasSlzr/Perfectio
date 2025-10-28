# /schemas/diary_schema.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# --- BASE SCHEMAS ---
class DiaryEntryBase(BaseModel):
    """Estructura base de una entrada del diario."""
    date: datetime
    content: str


class DiaryEntryCreate(DiaryEntryBase):
    """Schema para crear una nueva entrada."""
    pass


class DiaryEntry(DiaryEntryBase):
    """Schema completo de una entrada, incluyendo su ID y referencia al diario."""
    id_entry: int
    diary_id: int

    class Config:
        from_attributes = True


class DiaryBase(BaseModel):
    """Estructura base del Diario (asociado a un usuario)."""
    user_id: int


class DiaryCreate(DiaryBase):
    """Schema para crear un diario nuevo (por ejemplo, al registrar usuario)."""
    pass


class Diary(DiaryBase):
    """Schema completo de un diario, con sus entradas."""
    id_diary: int
    entries: Optional[list[DiaryEntry]] = []

    class Config:
        from_attributes = True
