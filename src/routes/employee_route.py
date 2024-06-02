# routes/employee_routes.py

from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List
from src.models.employee import Employee, EmployeeCreate, EmployeeBase
from src.service.employee_service import EmployeeService
from src.core.dependencies import get_employee_service
from src.auth.auth import authenticate

router = APIRouter()

@router.get("/api/v1/employees", response_model=List[Employee])
def view_employees(service: EmployeeService = Depends(get_employee_service), authorized: bool = Depends(authenticate)):
    return service.get_employees()

@router.get("/api/v1/employees/csv")
def download_employees_csv_endpoint(response: Response, service: EmployeeService = Depends(get_employee_service), authorized: bool = Depends(authenticate)):
    csv_data = service.get_employees_csv()
    response.headers["Content-Disposition"] = "attachment; filename=employees.csv"
    return Response(content=csv_data, media_type="text/csv")

@router.get("/api/v1/employees/{manpower_id}", response_model=Employee)
def get_employee_detail(manpower_id: str, service: EmployeeService = Depends(get_employee_service), authorized: bool = Depends(authenticate)):
    employee = service.get_employee_by_manpower_id(manpower_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.patch("/api/v1/employees/{manpower_id}", response_model=Employee)
def update_employee_endpoint(manpower_id: str, employee_data: EmployeeBase, service: EmployeeService = Depends(get_employee_service), authorized: bool = Depends(authenticate)):
    updated_employee = service.update_employee(manpower_id, employee_data.dict())
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.post("/api/v1/employees", response_model=Employee)
def create_employee_endpoint(employee: EmployeeCreate, service: EmployeeService = Depends(get_employee_service), authorized: bool = Depends(authenticate)):
    try:
        new_employee = service.create_employee(employee)
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
