# app/models/ia_assistant.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class IAAssistant(Base):
    __tablename__ = 'ia_assistants'
    id_ia = Column(Integer, primary_key=True, index=True)
    user_context = Column(Text)
    messages_history = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id_user'), unique=True)

    user = relationship("User", back_populates="ia_assistant")