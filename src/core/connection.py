import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.models.sample_manpower_list_model import SampleManpowerList

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = SampleManpowerList.metadata
metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Check if the table exists and create it if it doesn't
def create_tables_if_not_exist():
    inspector = inspect(engine)
    if not inspector.has_table("SampleManpowerList", schema="test"):
        SampleManpowerList.metadata.create_all(bind=engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Call the function to check and create tables
create_tables_if_not_exist()
