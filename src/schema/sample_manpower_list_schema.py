from pydantic import BaseModel
from typing import Optional
from datetime import date

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

class Employee(EmployeeBase):
    id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    designation: Optional[str] = None
    project: Optional[str] = None
    team: Optional[str] = None
    supervisor: Optional[str] = None
    joinDate: Optional[date] = None
    resignDate: Optional[date] = None