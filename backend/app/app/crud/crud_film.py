from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.film import Film
from app.models.utilisateur import Utilisateur
from app.schemas.film import FilmCreate, FilmUpdateRestricted, FilmUpdate


class CRUDFilm(CRUDBase[Film, FilmCreate, FilmUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Utilisateur,
        obj_in: Union[FilmUpdate, FilmUpdateRestricted]
    ) -> Film:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


film = CRUDFilm(Film)