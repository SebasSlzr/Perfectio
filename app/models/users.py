# app/models/users.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    habits = relationship("Habit", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    diary = relationship("Diary", back_populates="user", uselist=False)
    ia_assistant = relationship("IAAssistant", back_populates="user", uselist=False)
    user_achievements = relationship("UserAchievement", back_populates="user")