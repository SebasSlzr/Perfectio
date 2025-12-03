# app/models/diary_entry.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class DiaryEntry(Base):
    __tablename__ = 'diary_entries'
    id_entry = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    content = Column(Text, nullable=False)
    diary_id = Column(Integer, ForeignKey('diaries.id_diary'))

    diary = relationship("Diary", back_populates="entries")