import asyncio
from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import crud
from app.schemas.film import (
    Film,
    FilmCreate,
    FilmSearchResults,
    FilmUpdate,
)
from app.models.utilisateur import Utilisateur
from starlette.responses import Response


router = APIRouter()

@router.get("/", response_model=List[Film])
def get_all_films(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all films from the database.
    """
    films = crud.film.get_multi(db)
    return films


@router.get("/search/", status_code=200, response_model=FilmSearchResults)
def search_films(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="foudre"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for films based on label keyword
    """
    films = crud.film.get_multi(db=db, limit=max_results)
    results = filter(lambda film : keyword.lower() in film.label.lower(), films)
    return {"results": list(results)}


@router.get("/{film_id}", status_code=200, response_model=Film)
def fetch_film(
    *,
    film_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single film by ID
    """
    result = crud.film.get(db=db, id=film_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Film with ID {film_id} not found"
        )

    return result




@router.post("/film/", status_code=201, response_model=Film)
def create_film(
    *, film_in: FilmCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new film in the database.
    """
    film = crud.film.create(db=db, obj_in=film_in)
    return film



@router.put("/{film_id}", status_code=201, response_model=Film)
def update_film(
    *,
    # film_in: FilmUpdateRestricted,
    film_in: FilmUpdate,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> dict:
    """
    Update film in the database.
    """
    film = crud.film.get(db, id=film_in.id)
    if not film:
        raise HTTPException(
            status_code=400, detail=f"Film with ID: {film_in.id} not found."
        )

    # if film.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only update your films."
    #     )

    updated_film = crud.film.update(db=db, db_obj=film, obj_in=film_in)
    return updated_film



@router.delete("/{id}", status_code=204)
def delete_film(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> Any:
    """
    Delete a film from the database.
    """
    film = crud.film.get(db, id=id)
    if not film:
        raise HTTPException(
            status_code=404, detail=f"Film with ID: {id} not found."
        )

    # if film.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only delete your films."
    #     )

    crud.film.remove(db=db, id=id)
    return Response(status_code=204)