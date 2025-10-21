from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class IA_Assistant(Base):
    __tablename__ = 'ia_assistants'
    id_ia = Column(Integer, primary_key=True, index=True)
    user_context = Column(Text)
    messages_history = Column(Text)

    user_id = Column(Integer, ForeignKey('users.id_user'), unique=True)

 
    user = relationship("User", back_populates="ia_assistant")