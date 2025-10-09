from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

class Habit(Base):
    __tablename__ = 'habits'
    id_habit = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    tag = Column(String)
    start_date = Column(Date, nullable=False)
    frequency = Column(String, nullable=False)  # Ejemplo: "daily", "weekly"
    reminders = Column(Boolean, default=False)
    notes = Column(String)
    color = Column(String)
    icon = Column(String)
    state = Column(String, nullable=False)  # Ejemplo: "active", "inactive"

    # Claves foráneas
    user_id = Column(Integer, ForeignKey('users.id_user'))
    goal_id = Column(Integer, ForeignKey('goals.id_goal'), nullable=True)

    # Relaciones
    user = relationship("User", back_populates="habits")
    goal = relationship("Goal", back_populates="habits")
    reminders_list = relationship("Reminder", back_populates="habit")
