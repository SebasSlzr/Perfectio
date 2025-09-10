class Achievement(Base):
    __tablename__ = 'achievements'
    id_achievement = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False)

    # Clave foránea
    user_id = Column(Integer, ForeignKey('users.id_user'))

    # Relaciones
    user = relationship("User", back_populates="achievements")
    emblem = relationship("Emblem", back_populates="achievement", uselist=False)  # Relación 1:1
    reward = relationship("Reward", back_populates="achievement", uselist=False)
