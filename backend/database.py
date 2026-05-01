from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Ayush1234@localhost:5432/crud"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, bind=engine)