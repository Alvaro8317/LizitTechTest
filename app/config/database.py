from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = getenv("DB_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()
Base = declarative_base()


def get_database():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Unexpected error with the database, details: ", e)
    finally:
        db.close()
