from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:PKciPzjzWKNhNRSeffSliNtQvtKzMWnZ@shortline.proxy.rlwy.net:11714/railway'


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
