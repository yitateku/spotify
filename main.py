from fastapi import FastAPI
from models.base import Base
from routes import auth
from database import engine
from pydantic_schemas.user_create import UserCreate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app = FastAPI(debug=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev/testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/auth')

Base.metadata.create_all(bind=engine)
