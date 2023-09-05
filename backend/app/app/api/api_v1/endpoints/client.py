import asyncio
from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import crud
from app.schemas.client import (
    Client,
    ClientCreate,
    ClientSearchResults,
    ClientUpdate,
)
from app.models.film import Film
from starlette.responses import Response


router = APIRouter()

@router.get("/", response_model=List[Client])
def get_all_clients(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all clients from the database.
    """
    clients = crud.client.get_multi(db)
    return clients


@router.get("/search/", status_code=200, response_model=ClientSearchResults)
def search_clients(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="Client"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for clients based on label keyword
    """
    clients = crud.client.get_multi(db=db, limit=max_results)
    results = filter(lambda client : keyword.lower() in client.label.lower(), clients)
    return {"results": list(results)}


@router.get("/{client_id}", status_code=200, response_model=Client)
def fetch_client(
    *,
    client_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single client by ID
    """
    result = crud.client.get(db=db, id=client_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Client with ID {client_id} not found"
        )

    return result




@router.post("/client/", status_code=201, response_model=Client)
def create_client(
    *, client_in: ClientCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new client in the database.
    """
    client = crud.client.create(db=db, obj_in=client_in)
    return client



@router.put("/{client_id}", status_code=201, response_model=Client)
def update_client(
    *,
    # client_in: ClientUpdateRestricted,
    client_in: ClientUpdate,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> dict:
    """
    Update client in the database.
    """
    client = crud.client.get(db, id=client_in.id)
    if not client:
        raise HTTPException(
            status_code=400, detail=f"Client with ID: {client_in.id} not found."
        )

    # if client.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only update your clients."
    #     )

    updated_client = crud.client.update(db=db, db_obj=client, obj_in=client_in)
    return updated_client



@router.delete("/{id}", status_code=204)
def delete_client(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_utilisateur: Utilisateur = Depends(deps.get_current_utilisateur),
) -> Any:
    """
    Delete a client from the database.
    """
    client = crud.client.get(db, id=id)
    if not client:
        raise HTTPException(
            status_code=404, detail=f"Client with ID: {id} not found."
        )

    # if client.submitter_id != current_utilisateur.id:
    #     raise HTTPException(
    #         status_code=403, detail=f"You can only delete your clients."
    #     )

    crud.client.remove(db=db, id=id)
    return Response(status_code=204)