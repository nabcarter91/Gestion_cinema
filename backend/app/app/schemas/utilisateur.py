from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlalchemy import Sequence


class UtilisateurBase(BaseModel):
    role: Optional[str]
    nom: Optional[str]
    permissions: bool = False
    email: Optional[EmailStr] = None
    


# Properties to receive via API on creation
class UtilisateurCreate(UtilisateurBase):
    email: EmailStr
    motDePasse: str


# Properties to receive via API on update
class UtilisateurUpdate(UtilisateurBase):
    ...


class UtilisateurInDBBase(UtilisateurBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties stored in DB but not returned by API
class UtilisateurInDB(UtilisateurInDBBase):
    hashed_motDePasse: str

# Additional properties to return via API
class Utilisateur(UtilisateurInDBBase):
    pass

# class UtilisateurSearchResults(BaseModel):
#     results: Sequence[Utilisateur]
