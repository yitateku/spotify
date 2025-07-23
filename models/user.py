from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary
from models.base import Base


class UserBase(Base):
    __abstract__ = True  # This class won't be mapped to a table itself
    id = Column(TEXT, primary_key=True)


class User(UserBase):
    __tablename__ = 'users'

    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)
