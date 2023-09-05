from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


connection_uri = settings.SQLALCHEMY_DATABASE_URI
print("Database URL is ",connection_uri)

engine = create_engine(
    connection_uri,
    
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





#Sqlite3
# engine = create_engine(
#     settings.SQLALCHEMY_DATABASE_URI,
#     # required for sqlite
#     connect_args={"check_same_thread": False},
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
