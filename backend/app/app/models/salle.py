from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Salle(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    nom = Column(String(256), nullable=True)
    capacite = Column(Integer, nullable=False)
    equipements = Column(String(256), nullable=True)
    id_utilisateur = Column(Integer, ForeignKey("utilisateur.id"), nullable=True)
    submitter = relationship("Utilisateur", back_populates="salles")
    seances = relationship("Seance", back_populates="salles")
    sieges = relationship("Siege", back_populates="salles")
