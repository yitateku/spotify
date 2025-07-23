from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://musicapp:zl4kmkOtI2zGraV27yfyDzS0qmV089EO@dpg-d20dt37diees739dtjng-a/musicapp_ag86'


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
