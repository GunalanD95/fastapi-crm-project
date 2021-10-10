from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

SQLALCHEMY_DATABASE_URL = "sqlite:///crm-lead/crm.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
BASE_PATH = Path(__file__).resolve().parent

Base = declarative_base()

SessionLocal = sessionmaker(bind= engine , autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close