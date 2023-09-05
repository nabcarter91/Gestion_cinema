from fastapi import APIRouter

from app.api.api_v1.endpoints import film,auth,seance,reservation,client,salle,siege


api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(film.router, prefix="/films", tags=["films"])
api_router.include_router(client.router, prefix="/clients", tags=["clients"])
api_router.include_router(seance.router, prefix="/seances", tags=["seances"])
api_router.include_router(reservation.router, prefix="/reservations", tags=["reservations"])
api_router.include_router(salle.router, prefix="/salles", tags=["salles"])
api_router.include_router(siege.router, prefix="/sieges", tags=["sieges"])