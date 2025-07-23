from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres.gwkwtinjhitwegdhfcxv:O5CcxrTjU7Jm9WjI@aws-0-eu-north-1.pooler.supabase.com:6543/postgres'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
