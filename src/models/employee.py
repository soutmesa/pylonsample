from pydantic import BaseModel, validator
from sqlalchemy import Table, Column, Integer, String, Date, MetaData
from datetime import date
from typing import Optional

metadata = MetaData()

# SQLAlchemy table schema
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
    Column('resignDate', Date, nullable=True),
    schema='test'  # Specify the schema here
)

# Pydantic models
class EmployeeBase(BaseModel):
    nric4Digit: str
    name: str
    manpowerId: str
    designation: str
    project: str
    team: str
    supervisor: str
    joinDate: date
    resignDate: Optional[date] = None

    @validator('joinDate', 'resignDate', pre=True, always=True)
    def validate_dates(cls, value):
        if value is None:
            return value
        if isinstance(value, str):
            return date.fromisoformat(value)
        return value

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
