from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import engine, Base
from app.config import settings

from app.models import User

from app.routers.auth import router as auth_router
from app.routers.conversation import router as conversation_router
from app.routers.message import router as message_router
from app.routers.chat import router as chat_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME
)


# CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ROUTERS
app.include_router(auth_router)
app.include_router(conversation_router)
app.include_router(message_router)
app.include_router(chat_router)


@app.get("/")
def root():

    return {
        "message": "AI Chat Backend Running"
    }


@app.get("/db-check")
def db_check():

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "database": "connected"
    }