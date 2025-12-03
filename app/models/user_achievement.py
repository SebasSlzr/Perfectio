# app/models/user_achievement.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserAchievement(Base):
    __tablename__ = 'user_achievements'
    user_id = Column(Integer, ForeignKey('users.id_user'), primary_key=True)
    id_achievement = Column(Integer, ForeignKey('achievements.id_achievement'), primary_key=True)
    date_achieved = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="user_achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")