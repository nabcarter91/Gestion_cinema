from pydantic import BaseModel

from typing import Sequence


class SalleBase(BaseModel):
    nom: str
    capacite: int
    equipements:str
    id_utilisateur:int
  


class SalleCreate(SalleBase):
    nom: str
    capacité: int
    equipements:str
    id_utilisateur:int


class SalleUpdate(SalleBase):
    id: int
    nom: str
    capacité: int
    equipements:str
class SalleUpdateRestricted(BaseModel):
    id: int
    date: int

# Properties shared by models stored in DB
class SalleInDBBase(SalleBase):
    id: int
    id_utilisateur:int

    class Config:
        orm_mode = True


# Properties to return to client
class Salle(SalleInDBBase):
    pass


# Properties properties stored in DB
class SalleInDB(SalleInDBBase):
    pass


class SalleSearchResults(BaseModel):
    results: Sequence[Salle]

class SalleDelete(SalleBase):
    id: int