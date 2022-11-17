from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
SQLALCHEMY_DATABASE_URL = "postgresql://postgres@localhost:5432/komroom"

# Create a DeclarativeMeta instance

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
