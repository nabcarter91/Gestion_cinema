from sqlalchemy import Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

#Association table
association_table=Table("utilisateur_client",Base.metadata,
                         Column("id_utilisateur",ForeignKey('utilisateur.id'), primary_key=True),
                         Column("id_client",ForeignKey('client.id'), nullable=True),
                         )

class Client(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    nom = Column(String(256), nullable=True)
    prenom = Column(String(256), nullable=True)
    email = Column(String(256), nullable=True)
    telephone = Column(String(256), nullable=True)
    dateNaissance = Column(String(256), nullable=True)
    adresse = Column(String(256), nullable=True)
    abonnement = Column(String(256), nullable=True)
    carteFidelite = Column(String(256), nullable=True)
    submitter = relationship("Utilisateur",secondary=association_table, back_populates="clients")
    reservations = relationship(
        "Reservation",
        cascade="all,delete-orphan",
        back_populates="clients",
        uselist=True,
    )