# app/models/achievement.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Achievement(Base):
    __tablename__ = 'achievements'
    id_achievement = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    image_url = Column(String(255))
    points_awarded = Column(Integer)

    user_achievements = relationship("UserAchievement", back_populates="achievement")