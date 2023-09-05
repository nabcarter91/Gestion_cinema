from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.siege import Siege
from app.models.utilisateur import Utilisateur
from app.schemas.siege import SiegeCreate, SiegeUpdateRestricted, SiegeUpdate


class CRUDSiege(CRUDBase[Siege, SiegeCreate, SiegeUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[SiegeUpdate, SiegeUpdateRestricted]
    ) -> Siege:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj

siege = CRUDSiege(Siege)