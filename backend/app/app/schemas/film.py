from pydantic import BaseModel, HttpUrl

from typing import Sequence


class FilmBase(BaseModel):
    titre: str
    duree: str
    synopsis: str
    genre:str
    realisateur:str
    acteurs:str
    classification:str
    urlBandeAnnonce:HttpUrl
    urlAffiche:HttpUrl
    


class FilmCreate(FilmBase):
    titre: str
    duree: int
    urlBandeAnnonce:HttpUrl
    id_utilisateur: int


class FilmUpdate(FilmBase):
    id: int
    titre: str
    synopsis: str
    urlBandeAnnonce:HttpUrl

class FilmUpdateRestricted(BaseModel):
    id: int
    titre: str

# Properties shared by models stored in DB
class FilmInDBBase(FilmBase):
    id: int
    id_utilisateur: int

    class Config:
        orm_mode = True


# Properties to return to client
class Film(FilmInDBBase):
    pass


# Properties properties stored in DB
class FilmInDB(FilmInDBBase):
    pass


class FilmSearchResults(BaseModel):
    results: Sequence[Film]

class FilmDelete(FilmBase):
    id: int