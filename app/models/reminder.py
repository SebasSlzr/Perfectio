# app/models/reminder.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Reminder(Base):
    __tablename__ = 'reminders'
    id_reminder = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    shouldRepeat = Column(Boolean, default=False)
    habit_id = Column(Integer, ForeignKey('habits.id_habit'), nullable=False)

    habit = relationship("Habit", back_populates="reminders_rel")