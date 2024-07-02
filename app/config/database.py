from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://lizit:l1z1t4dm1n@localhost/lizit"
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
