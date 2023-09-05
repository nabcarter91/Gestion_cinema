from pydantic import BaseModel

from typing import Sequence


class SiegeBase(BaseModel):
    nbreSieges: int
    typeSieges: str
    id_Siege:int
  


class SiegeCreate(SiegeBase):
    nbreSieges: int
    typeSieges: str
    id_salle:int


class SiegeUpdate(SiegeBase):
    id: int
    nbreSieges: int
    typeSieges: str
class SiegeUpdateRestricted(BaseModel):
    id: int
    nbreSieges: int

# Properties shared by models stored in DB
class SiegeInDBBase(SiegeBase):
    id: int
    id_Siege:int

    class Config:
        orm_mode = True


# Properties to return to client
class Siege(SiegeInDBBase):
    pass


# Properties properties stored in DB
class SiegeInDB(SiegeInDBBase):
    pass


class SiegeSearchResults(BaseModel):
    results: Sequence[Siege]

class SiegeDelete(SiegeBase):
    id: int