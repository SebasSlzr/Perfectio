from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Reminder(Base):
    __tablename__ = 'reminders'
    id_reminder = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    shouldRepeat = Column(Boolean, default=False)

  
    habit_id = Column(Integer, ForeignKey('habits.id_habit'))
