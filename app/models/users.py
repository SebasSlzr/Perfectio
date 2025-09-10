from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    # Relaciones
    habits = relationship("Habit", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    diary = relationship("Diary", back_populates="user", uselist=False)
    achievements = relationship("Achievement", back_populates="user")
    ia_assistant = relationship("IA_Assistant", back_populates="user", uselist=False)
