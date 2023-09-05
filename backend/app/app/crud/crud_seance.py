from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.seance import Seance
from app.models.utilisateur import Utilisateur
from app.schemas.seance import SeanceCreate, SeanceUpdateRestricted, SeanceUpdate


class CRUDSeance(CRUDBase[Seance, SeanceCreate, SeanceUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[SeanceUpdate, SeanceUpdateRestricted]
    ) -> Seance:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


seance = CRUDSeance(Seance)