from fastapi import FastAPI
from settings import database
from models import models
from routes import users, orders, admin, auth
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
from contextlib import asynccontextmanager
import asyncio
from sqlalchemy import text

@asynccontextmanager
async def main_app(app: FastAPI):
    while True:
        try:
            db = next(database.get_db())
            db.execute(text("SELECT 1"))
            break
        except OperationalError:
            print("Database is not ready, waiting...")
            await asyncio.sleep(1)
    models.Base.metadata.create_all(bind=database.engine)
    yield

app= FastAPI(
    lifespan=main_app,
    title="E-Commerce API",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)

@app.get("/")
def read_base():
    return {"message": "Welcome to the E-Commerce API"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(admin.router)
