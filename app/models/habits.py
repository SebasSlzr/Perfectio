# app/models/habits.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Habit(Base):
    __tablename__ = 'habits'
    id_habit = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    tag = Column(String)
    start_date = Column(Date, nullable=False)
    frequency = Column(String)
    color = Column(String)
    icon = Column(String)
    state = Column(String, default="activo")
    user_id = Column(Integer, ForeignKey('users.id_user'))

    user = relationship("User", back_populates="habits")
    reminders_rel = relationship("Reminder", back_populates="habit")
    goal_habits = relationship("GoalHabit", back_populates="habit")