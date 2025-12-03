# app/models/goal_habit.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class GoalHabit(Base):
    __tablename__ = 'goal_habit'
    id_goal = Column(Integer, ForeignKey('goals.id_goal'), primary_key=True)
    id_habit = Column(Integer, ForeignKey('habits.id_habit'), primary_key=True)

    goal = relationship("Goal", back_populates="goal_habits")
    habit = relationship("Habit", back_populates="goal_habits")