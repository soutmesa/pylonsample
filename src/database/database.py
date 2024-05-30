from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

SampleManpowerList = Table(
    'SampleManpowerList', metadata,
    Column('id', Integer, primary_key=True),
    Column('nric4Digit', String(50)),
    Column('name', String(50)),
    Column('manpowerId', String(50)),
    Column('designation', String(50)),
    Column('project', String(50)),
    Column('team', String(50)),
    Column('supervisor', String(50)),
    Column('joinDate', Date),
    Column('resignDate', Date, nullable=True)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_employees(db):
    query = select([SampleManpowerList])
    return db.execute(query).fetchall()

def update_employee(db, manpower_id, employee_data):
    update_data = {k: v for k, v in employee_data.items() if v is not None}
    query = SampleManpowerList.update().where(SampleManpowerList.c.manpowerId == manpower_id).values(update_data)
    result = db.execute(query)
    if result.rowcount == 0:
        raise ValueError("Employee not found")
    return {"message": "Employee details updated successfully"}

def get_employees_csv(db):
    employees = get_employees(db)
    df = pd.DataFrame(employees)
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return output.getvalue()
