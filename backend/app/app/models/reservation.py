from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Reservation(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    siegesReserves = Column(Integer, nullable=False)
    montant = Column(Integer, nullable=False)
    status = Column(Boolean, default=False)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=True)
    clients = relationship("Client", back_populates="reservations")
    id_seance = Column(Integer, ForeignKey("seance.id"), nullable=True)
    seances = relationship("Seance", back_populates="reservations")
   
