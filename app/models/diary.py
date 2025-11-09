# app/models/diary.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Diary(Base):
    __tablename__ = 'diaries'
    id_diary = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id_user'), unique=True)

    user = relationship("User", back_populates="diary")
    entries = relationship("DiaryEntry", back_populates="diary")