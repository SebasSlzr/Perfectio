from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Diary(Base):
    __tablename__ = 'diaries'
    id_diary = Column(Integer, primary_key=True, index=True)

    # Clave foránea
    user_id = Column(Integer, ForeignKey('users.id_user'), unique=True)

    # Relación
    user = relationship("User", back_populates="diary")
    entries = relationship("Diary_Entry", back_populates="diary")