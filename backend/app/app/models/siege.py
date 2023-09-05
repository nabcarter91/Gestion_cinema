from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Siege(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    nbreSieges = Column(Integer, nullable=False)
    typeSieges = Column(String(256), nullable=True)
    id_salle = Column(Integer, ForeignKey("salle.id"), nullable=True)
    salles = relationship("Salle", back_populates="sieges")
