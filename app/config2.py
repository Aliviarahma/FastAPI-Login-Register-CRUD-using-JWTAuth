from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = 'postgresql://postgres:dbnetmonk!@localhost:5433/embed_dash'
DATABASE_URL = 'postgresql://postgres:dbnetmonk!@172.17.0.1:5432/embed_dash'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
