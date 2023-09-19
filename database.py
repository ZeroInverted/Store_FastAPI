from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


DATABASE_URL = "sqlite:///store.db"

engine = create_engine(DATABASE_URL)

# Scoped sessions for thread-local sessions and easy session instantiation through db_session()
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def get_db() -> db_session:
    db = db_session()
    try:
        yield db
    finally:
        db.close()
