from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from src.models.employee import EmployeeCreate, Employee, EmployeeBase
from src.database.connection import get_db_session
from src.auth.auth import authenticate
from src.service.employee_service import get_employees, update_employee, create_employee, get_employees_csv, get_employee_by_manpower_id
router = APIRouter()

@router.get("/api/v1/employees", response_model=List[Employee])
def view_employees(db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    return get_employees(db)

@router.get("/api/v1/employees/csv")
def download_employees_csv_endpoint(response: Response, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    csv_data = get_employees_csv(db)
    response.headers["Content-Disposition"] = "attachment; filename=employees.csv"
    return Response(content=csv_data, media_type="text/csv")

@router.get("/api/v1/employees/{manpower_id}", response_model=Employee)
def get_employee_detail(manpower_id: str, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    employee = get_employee_by_manpower_id(db, manpower_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.patch("/api/v1/employees/{manpower_id}", response_model=Employee)
def update_employee_endpoint(manpower_id: str, employee_data: EmployeeBase, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    updated_employee = update_employee(db, manpower_id, employee_data.dict())
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.post("/api/v1/employees", response_model=Employee)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    try:
        new_employee = create_employee(db, employee.dict())
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))