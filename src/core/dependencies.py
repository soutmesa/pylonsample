from fastapi import Depends
from sqlalchemy.orm import Session
from ..service.employee_service import EmployeeService
from .connection import get_db_session

def get_employee_service(db: Session = Depends(get_db_session)) -> EmployeeService:
    return EmployeeService(db)
