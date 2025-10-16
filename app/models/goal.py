from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship

class Goal(Base):
    __tablename__ = 'goals'
    id_goal = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    progress = Column(Float, default=0.0)

    # Claves foráneas
    user_id = Column(Integer, ForeignKey('users.id_user'))

    # Relaciones
    user = relationship("User", back_populates="goals")
    habits = relationship("Habit", back_populates="goal")

