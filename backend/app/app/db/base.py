# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.utilisateur import Utilisateur  # noqa
from app.models.film import Film
from app.models.seance import Seance # noqa
from app.models.reservation import Reservation # noqa
from app.models.client import Client # noqa
