from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

#from app.database import Base

class Pets():
    __tablename__ = 'pets'

    id_event = Column(Integer, primary_key=True, index=True)
    pet_name = Column(String, nullable=False)
    race = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)) #cambiar a integer
    initial_weigth = Column(DateTime, nullable=True) #cambiar a float
    owner = Column(String, nullable=False)

    # Relaciones
    state = relationship("State", back_populates="pets")