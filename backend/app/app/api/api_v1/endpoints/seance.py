import asyncio
from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import crud
from app.schemas.seance import (
    Seance,
    SeanceCreate,
    SeanceSearchResults,
    SeanceUpdate,
)
from app.models.film import Film
from starlette.responses import Response


router = APIRouter()

@router.get("/", response_model=List[Seance])
def get_all_seances(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all seances from the database.
    """
    seances = crud.seance.get_multi(db)
    return seances


@router.get("/search/", status_code=200, response_model=SeanceSearchResults)
def search_seances(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="seance"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for seances based on label keyword
    """
    seances = crud.seance.get_multi(db=db, limit=max_results)
    results = filter(lambda seance : keyword.lower() in seance.label.lower(), seances)
    return {"results": list(results)}


@router.get("/{seance_id}", status_code=200, response_model=Seance)
def fetch_seance(
    *,
    seance_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single seance by ID
    """
    result = crud.seance.get(db=db, id=seance_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Seance with ID {seance_id} not found"
        )

    return result




@router.post("/seance/", status_code=201, response_model=Seance)
def create_seance(
    *, seance_in: SeanceCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new seance in the database.
    """
    seance = crud.seance.create(db=db, obj_in=seance_in)
    return seance



@router.put("/{seance_id}", status_code=201, response_model=Seance)
def update_seance(
    *,
    # seance_in: SeanceUpdateRestricted,
    seance_in: SeanceUpdate,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> dict:
    """
    Update seance in the database.
    """
    seance = crud.seance.get(db, id=seance_in.id)
    if not seance:
        raise HTTPException(
            status_code=400, detail=f"Seance with ID: {seance_in.id} not found."
        )

    # if seance.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only update your seances."
    #     )

    updated_seance = crud.seance.update(db=db, db_obj=seance, obj_in=seance_in)
    return updated_seance



@router.delete("/{id}", status_code=204)
def delete_seance(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> Any:
    """
    Delete a seance from the database.
    """
    seance = crud.seance.get(db, id=id)
    if not seance:
        raise HTTPException(
            status_code=404, detail=f"Seance with ID: {id} not found."
        )

    # if seance.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only delete your seances."
    #     )

    crud.seance.remove(db=db, id=id)
    return Response(status_code=204)