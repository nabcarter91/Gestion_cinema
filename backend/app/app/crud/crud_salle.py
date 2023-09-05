from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.salle import Salle
from app.models.utilisateur import Utilisateur
from app.schemas.salle import SalleCreate, SalleUpdateRestricted, SalleUpdate


class CRUDSalle(CRUDBase[Salle, SalleCreate, SalleUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[SalleUpdate, SalleUpdateRestricted]
    ) -> Salle:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


salle = CRUDSalle(Salle)