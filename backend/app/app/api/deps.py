from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.utilisateur import Utilisateur
from app import crud


class TokenData(BaseModel):
    nom: Optional[str] = None


def get_db() -> Generator:
    db = SessionLocal()
    db.current_utilisateur_id = None
    try:
        yield db
    finally:
        db.close()


async def get_current_utilisateur(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> Utilisateur:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.deecode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        nom: str = payload.get("sub")
        if nom is None:
            raise credentials_exception
        token_data = TokenData(nom=nom)
    except JWTError:
        raise credentials_exception

    utilisateur = db.query(utilisateur).filter(utilisateur.id == token_data.nom).first()
    if utilisateur is None:
        raise credentials_exception
    return utilisateur


def get_current_active_superutilisateur(
    current_utilisateur: Utilisateur = Depends(get_current_utilisateur),
) -> Utilisateur:
    if not crud.utilisateur.permissions(current_utilisateur):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_utilisateur