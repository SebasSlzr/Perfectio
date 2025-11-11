# app/models/habits.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Habit(Base):
    __tablename__ = 'habits'
    id_habit = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)       
    tag = Column(String(50))                            
    start_date = Column(Date, nullable=False)
    frequency = Column(String(20))                    
    color = Column(String(20))                           
    icon = Column(String(50))                            
    state = Column(String(20), default="activo")        
    user_id = Column(Integer, ForeignKey('users.id_user'))

    user = relationship("User", back_populates="habits")
    reminders_rel = relationship("Reminder", back_populates="habit")
    goal_habits = relationship("GoalHabit", back_populates="habit")