from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Creamos la base de datos local llamada 'conversiones.db'
DATABASE_URL = "sqlite:///conversiones.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)
