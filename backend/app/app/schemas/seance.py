from pydantic import BaseModel

from typing import Sequence


class SeanceBase(BaseModel):
    date: int
    heure: int
    tarifs:int
    id_film:int
    id_salle:int
  


class SeanceCreate(SeanceBase):
    date: int
    heure: str
    tarifs:str
    id_film:int
    id_salle:int
    id_reservation:int


class SeanceUpdate(SeanceBase):
    id: int
    date: int
    heure: str
    tarifs:str
class SeanceUpdateRestricted(BaseModel):
    id: int
    date: int

# Properties shared by models stored in DB
class SeanceInDBBase(SeanceBase):
    id: int
    id_film:int
    id_salle:int

    class Config:
        orm_mode = True


# Properties to return to client
class Seance(SeanceInDBBase):
    pass


# Properties properties stored in DB
class SeanceInDB(SeanceInDBBase):
    pass


class SeanceSearchResults(BaseModel):
    results: Sequence[Seance]

class SeanceDelete(SeanceBase):
    id: int