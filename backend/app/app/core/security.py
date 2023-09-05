from passlib.context import CryptContext


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_motDePasse(plain_motDePasse: str, hashed_motDePasse: str) -> bool:
    return PWD_CONTEXT.verify(plain_motDePasse, hashed_motDePasse)


def get_motDePasse_hash(motDePasse: str) -> str:
    return PWD_CONTEXT.hash(motDePasse)