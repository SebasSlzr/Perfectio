# app/models/diary_entry.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DiaryEntry(Base):
    __tablename__ = 'diary_entries'
    id_entry = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    content = Column(String, nullable=False)
    diary_id = Column(Integer, ForeignKey('diaries.id_diary'))

    diary = relationship("Diary", back_populates="entries")