from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from app.models.utilisateur import Utilisateur
from app.schemas.reservation import ReservationCreate, ReservationUpdateRestricted, ReservationUpdate


class CRUDReservation(CRUDBase[Reservation, ReservationCreate, ReservationUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[ReservationUpdate, ReservationUpdateRestricted]
    ) -> Reservation:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


reservation = CRUDReservation(Reservation)