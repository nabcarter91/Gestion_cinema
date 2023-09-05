from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.client import Client
from app.models.utilisateur import Utilisateur
from app.schemas.client import ClientCreate, ClientUpdateRestricted, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[ClientUpdate, ClientUpdateRestricted]
    ) -> Client:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


client = CRUDClient(Client)