import asyncio
from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import crud
from app.schemas.reservation import (
    Reservation,
    ReservationCreate,
    ReservationSearchResults,
    ReservationUpdate,
)
from app.models.utilisateur import Utilisateur
from starlette.responses import Response


router = APIRouter()

@router.get("/", response_model=List[Reservation])
def get_all_Reservations(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all Reservations from the database.
    """
    Reservations = crud.reservation.get_multi(db)
    return Reservations


@router.get("/search/", status_code=200, response_model=ReservationSearchResults)
def search_Reservations(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="reservation"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Reservations based on label keyword
    """
    Reservations = crud.Reservation.get_multi(db=db, limit=max_results)
    results = filter(lambda Reservation : keyword.lower() in Reservation.label.lower(), Reservations)
    return {"results": list(results)}


@router.get("/{Reservation_id}", status_code=200, response_model=Reservation)
def fetch_Reservation(
    *,
    Reservation_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single Reservation by ID
    """
    result = crud.Reservation.get(db=db, id=Reservation_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Reservation with ID {Reservation_id} not found"
        )

    return result




@router.post("/Reservation/", status_code=201, response_model=Reservation)
def create_Reservation(
    *, Reservation_in: ReservationCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new Reservation in the database.
    """
    Reservation = crud.Reservation.create(db=db, obj_in=Reservation_in)
    return Reservation



@router.put("/{Reservation_id}", status_code=201, response_model=Reservation)
def update_Reservation(
    *,
    # Reservation_in: ReservationUpdateRestricted,
    Reservation_in: ReservationUpdate,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> dict:
    """
    Update Reservation in the database.
    """
    Reservation = crud.Reservation.get(db, id=Reservation_in.id)
    if not Reservation:
        raise HTTPException(
            status_code=400, detail=f"Reservation with ID: {Reservation_in.id} not found."
        )

    # if Reservation.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only update your Reservations."
    #     )

    updated_Reservation = crud.Reservation.update(db=db, db_obj=Reservation, obj_in=Reservation_in)
    return updated_Reservation



@router.delete("/{id}", status_code=204)
def delete_Reservation(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> Any:
    """
    Delete a Reservation from the database.
    """
    Reservation = crud.Reservation.get(db, id=id)
    if not Reservation:
        raise HTTPException(
            status_code=404, detail=f"Reservation with ID: {id} not found."
        )

    # if Reservation.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only delete your Reservations."
    #     )

    crud.Reservation.remove(db=db, id=id)
    return Response(status_code=204)