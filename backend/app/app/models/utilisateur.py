from sqlalchemy import ForeignKey, Integer, String, Column, Boolean,Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.client import association_table


class Utilisateur(Base):
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(256), nullable=True)
    nom = Column(String(256), nullable=True)
    permissions = Column(Boolean, default=False)
    email = Column(String(256), index=True, nullable=False)
    
    films = relationship(
        "Film",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )
    
    clients = relationship(
        "Client",
        back_populates="submitter",
        secondary=association_table,
        uselist=True,
    )
    
    
    salles = relationship(
        "Salle",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )
    
    hashed_motDePasse = Column(String(256), nullable=False)
