from pydantic import BaseModel

from typing import Sequence


class ReservationBase(BaseModel):
    id_client:int
    id_seance:int
    siegesReserves:int
    montant: int
    status: bool = False
  


class ReservationCreate(ReservationBase):
    id_client:int
    id_seance:int
    siegesReserves:int
    montant: int
    status: bool = False


class ReservationUpdate(ReservationBase):
    id_client:int
    id_seance:int
    siegesReserves:int
    montant: int
    status: bool = False
    
class ReservationUpdateRestricted(BaseModel):
    id: int
    siegesReserves:int

# Properties shared by models stored in DB
class ReservationInDBBase(ReservationBase):
    id: int
    id_client:int
    id_seance:int

    class Config:
        orm_mode = True


# Properties to return to client
class Reservation(ReservationInDBBase):
    pass


# Properties properties stored in DB
class ReservationInDB(ReservationInDBBase):
    pass


class ReservationSearchResults(BaseModel):
    results: Sequence[Reservation]

class ReservationDelete(ReservationBase):
    id: int