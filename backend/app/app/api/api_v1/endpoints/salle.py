import asyncio
from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import crud
from app.schemas.salle import (
    Salle,
    SalleCreate,
    SalleSearchResults,
    SalleUpdate,
)
from app.models.film import Film
from starlette.responses import Response


router = APIRouter()

@router.get("/", response_model=List[Salle])
def get_all_salles(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all salles from the database.
    """
    salles = crud.salle.get_multi(db)
    return salles


@router.get("/search/", status_code=200, response_model=SalleSearchResults)
def search_salles(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="salle"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for salles based on label keyword
    """
    salles = crud.salle.get_multi(db=db, limit=max_results)
    results = filter(lambda salle : keyword.lower() in salle.label.lower(), salles)
    return {"results": list(results)}


@router.get("/{salle_id}", status_code=200, response_model=Salle)
def fetch_salle(
    *,
    salle_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single salle by ID
    """
    result = crud.salle.get(db=db, id=salle_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Salle with ID {salle_id} not found"
        )

    return result




@router.post("/salle/", status_code=201, response_model=Salle)
def create_salle(
    *, salle_in: SalleCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new salle in the database.
    """
    salle = crud.salle.create(db=db, obj_in=salle_in)
    return salle



@router.put("/{salle_id}", status_code=201, response_model=Salle)
def update_salle(
    *,
    # salle_in: SalleUpdateRestricted,
    salle_in: SalleUpdate,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> dict:
    """
    Update salle in the database.
    """
    salle = crud.salle.get(db, id=salle_in.id)
    if not salle:
        raise HTTPException(
            status_code=400, detail=f"Salle with ID: {salle_in.id} not found."
        )

    # if salle.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only update your salles."
    #     )

    updated_salle = crud.salle.update(db=db, db_obj=salle, obj_in=salle_in)
    return updated_salle



@router.delete("/{id}", status_code=204)
def delete_salle(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> Any:
    """
    Delete a salle from the database.
    """
    salle = crud.salle.get(db, id=id)
    if not salle:
        raise HTTPException(
            status_code=404, detail=f"Salle with ID: {id} not found."
        )

    # if salle.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only delete your salles."
    #     )

    crud.salle.remove(db=db, id=id)
    return Response(status_code=204)