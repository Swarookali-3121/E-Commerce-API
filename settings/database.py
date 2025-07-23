from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from .util_env import Environment

env = Environment()
url = env.DATABASE_URL
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine,autoflush=True)
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()