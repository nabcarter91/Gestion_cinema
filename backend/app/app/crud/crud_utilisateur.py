from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.utilisateur import Utilisateur
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurUpdate
from app.core.security import get_motDePasse_hash


class CRUDUtilisateur(CRUDBase[Utilisateur, UtilisateurCreate, UtilisateurUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Utilisateur]:
        return db.query(Utilisateur).filter(Utilisateur.email == email).first()

    def create(self, db: Session, *, obj_in: UtilisateurCreate) -> Utilisateur:
        create_data = obj_in.dict()
        create_data.pop("motDePasse")
        db_obj = Utilisateur(**create_data)
        db_obj.hashed_motDePasse = get_motDePasse_hash(obj_in.motDePasse)
        db.add(db_obj)
        db.commit()

        return db_obj

    def update(
        self, db: Session, *, db_obj: Utilisateur, obj_in: Union[UtilisateurUpdate, Dict[str, Any]]
    ) -> Utilisateur:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def permissions(self, utilisateur: Utilisateur) -> bool:
        return utilisateur.permissions


utilisateur = CRUDUtilisateur(Utilisateur)