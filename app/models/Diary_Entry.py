from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Diary_Entry(Base):
    __tablename__ = 'diary_entries'
    id_entry = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    content = Column(String, nullable=False)

    # Clave foránea
    diary_id = Column(Integer, ForeignKey('diaries.id_diary'))

   
    diary = relationship("Diary", back_populates="entries")
