from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Seance(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    date = Column(Integer, nullable=False)
    heure = Column(Integer, nullable=False)
    tarifs = Column(Integer, nullable=False)
    id_film = Column(Integer, ForeignKey("film.id"), nullable=True)
    films = relationship("Film", back_populates="seances")
    reservations = relationship("Reservation", back_populates="seances")
    id_salle = Column(Integer, ForeignKey("salle.id"), nullable=True)
    salles = relationship("Salle", back_populates="seances")
