# app/models/goal.py
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Goal(Base):
    __tablename__ = 'goals'
    id_goal = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    progress = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey('users.id_user'), nullable=False)

    user = relationship("User", back_populates="goals")
    goal_habits = relationship("GoalHabit", back_populates="goal")