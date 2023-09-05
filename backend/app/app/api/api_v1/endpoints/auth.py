from ast import List
from typing import Any,List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps
from app.core.auth import (
    authenticate,
    create_access_token,
)
from app.models.utilisateur import Utilisateur

router = APIRouter()




# @router.get("/", response_model=List[Utilisateur])
# def get_all_utilisateur(
#     *,
#     db: Session = Depends(deps.get_db),
# ) -> Any:
#     """
#     Retrieve all utilisateur from the database.
#     """
#     utilisateur = crud.utilisateur.get_multi(db)
#     return utilisateur


@router.post("/login")
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Get the JWT for a utilisateur with data from OAuth2 request form body.
    """

    utilisateur = authenticate(email=form_data.nom, motDePasse=form_data.motDePasse, db=db)
    if not utilisateur:
        raise HTTPException(status_code=400, detail="Incorrect nom or motDePasse")

    return {
        "access_token": create_access_token(sub=utilisateur.id),
        "token_type": "bearer",
    }


@router.get("/me", response_model=schemas.Utilisateur)
def read_utilisateurs_me(current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur)):
    """
    Fetch the current logged in user.
    """

    utilisateur = current_utilisateur
    return utilisateur


@router.post("/signup", response_model=schemas.Utilisateur, status_code=201)
def create_utilisateur_signup(
    *,
    db: Session = Depends(deps.get_db),
    utilisateur_in: schemas.utilisateur.UtilisateurCreate,
) -> Any:
    """
    Create new user without the need to be logged in.
    """

    utilisateur = db.query(Utilisateur).filter(Utilisateur.email == utilisateur_in.email).first()
    if utilisateur:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    utilisateur = crud.utilisateur.create(db=db, obj_in=utilisateur_in)

    return utilisateur