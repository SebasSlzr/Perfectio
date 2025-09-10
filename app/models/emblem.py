from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Emblem(Base):
    __tablename__ = 'emblems'
    id_emblem = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # Clave foránea (relación 1:1 con Achievement)
    achievement_id = Column(Integer, ForeignKey('achievements.id_achievement'), unique=True)

    # Relación
    achievement = relationship("Achievement", back_populates="emblem")
