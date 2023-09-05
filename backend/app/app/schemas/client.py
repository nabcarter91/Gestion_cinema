from pydantic import BaseModel, EmailStr

from typing import Sequence


class ClientBase(BaseModel):
    nom: str
    prenom:str
    email:EmailStr
    telephone:str
    dateNaissance:str
    adresse:str
    abonnement:str
    carteFidelite:str
    abonnement:str
  


class ClientCreate(ClientBase):
    nom: str
    prenom:str
    email:EmailStr
    telephone:str
    dateNaissance:str
    adresse:str
    abonnement:str
    carteFidelite:str
    abonnement:str


class ClientUpdate(ClientBase):
    nom: str
    prenom:str
    email:EmailStr
    telephone:str
    dateNaissance:str
    adresse:str
    
class ClientUpdateRestricted(BaseModel):
    id: int
    nom: str

# Properties shared by models stored in DB
class ClientInDBBase(ClientBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Client(ClientInDBBase):
    pass


# Properties properties stored in DB
class ClientInDB(ClientInDBBase):
    pass


class ClientSearchResults(BaseModel):
    results: Sequence[Client]

class ClientDelete(ClientBase):
    id: int