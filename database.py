from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import databases


DATABASE_URL = "sqlite:///./store.db"
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

base = DeclarativeBase()

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
