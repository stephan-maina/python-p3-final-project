from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_manager.models import Base

DATABASE_URL = 'sqlite:///task_manager.db'  # You can use a different database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_database():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
