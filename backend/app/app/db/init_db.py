import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.core.config import settings

logger = logging.getLogger(__name__)

FILMS = [
    {
        "id": 1,
        "titre": "Foudre blanche",
        "duree": "120",
        "synopsis": "Foudre blanche src",
        "genre": "Film genre",
        "realisateur": "Foudre blanche src",
        "acteurs": "Foudre blanche src",
        "classification": "Foudre blanche src",
        "urlBandeAnnonce": "https://youtu.be/ss7DMZ7Vahk",
        "urlAffiche": "https://youtu.be/ss7DMZ7Vahk",
        "id_utilisateur": "0",
        
         
      
    },
    {
        "id": 2,
        "titre": "Foudre blanche",
        "duree": "120",
        "synopsis": "Foudre blanche src",
        "genre": "Film genre",
        "realisateur": "Foudre blanche src",
        "acteurs": "Foudre blanche src",
        "classification": "Foudre blanche src",
        "urlBandeAnnonce": "https://youtu.be/ss7DMZ7Vahk",
        "urlAffiche": "https://youtu.be/ss7DMZ7Vahk",
        "id_utilisateur": "0",
    },
    {
       "id": 3,
        "titre": "Foudre blanche",
        "duree": "120",
        "synopsis": "Foudre blanche src",
        "genre": "Film genre",
        "realisateur": "Foudre blanche src",
        "acteurs": "Foudre blanche src",
        "classification": "Foudre blanche src",
        "urlBandeAnnonce": "https://youtu.be/ss7DMZ7Vahk",
        "urlAffiche": "https://youtu.be/ss7DMZ7Vahk",
        "id_utilisateur": "0",  # noqa
    },
]


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    if settings.FIRST_SUPERUSER:
        utilisateur = crud.utilisateur.get_by_email(db, email=settings.FIRST_SUPERUSER)
        if not utilisateur:
            utilisateur_in = schemas.UtilisateurCreate(
                role="Admin-role",
                nom="Initial Super User",
                permissions=True,
                email=settings.FIRST_SUPERUSER,
                motDePasse=settings.FIRST_SUPERUSER,
            )
            utilisateur = crud.utilisateur.create(db, obj_in=utilisateur_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{settings.FIRST_SUPERUSER} already exists. "
            )
        if not utilisateur.films:
            for film in FILMS:
                film_in = schemas.FilmCreate(
                    titre=film["titre"],
                    duree=film["duree"],
                    synopsis=film["synopsis"],
                    genre=film["genre"],
                    realisateur=film["realisateur"],
                    acteurs=film["acteurs"],
                    classification=film["classification"],
                    urlBandeAnnonce=film["urlBandeAnnonce"],
                    urlAffiche=film["urlAffiche"],
                    id_utilisateur=utilisateur.id,
                )
                crud.film.create(db, obj_in=film_in)
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=nsfabrice2009@gmail.com"
        )