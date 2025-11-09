# app/models/achievement.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Achievement(Base):
    __tablename__ = 'achievements'
    id_achievement = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)
    points_awarded = Column(Integer)

    user_achievements = relationship("UserAchievement", back_populates="achievement")