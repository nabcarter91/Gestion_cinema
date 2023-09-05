from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Film(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    titre = Column(String(256), nullable=False)
    duree = Column(String(256), nullable=False)
    synopsis = Column(String(256), nullable=False)
    genre = Column(String(256), nullable=False)
    realisateur = Column(String(256), nullable=False)
    acteurs = Column(String(256), nullable=False)
    classification = Column(String(256), nullable=False)
    urlBandeAnnonce = Column(String(256), index=True, nullable=True)
    urlAffiche = Column(String(256), index=True, nullable=True)
    id_utilisateur = Column(Integer, ForeignKey("utilisateur.id"), nullable=True)
    submitter = relationship("Utilisateur", back_populates="films")
    seances = relationship("Seance", back_populates="films")
