from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import StreamingResponse
from io import StringIO
from typing import List
from src.schema.sample_manpower_list_schema import EmployeeCreate, Employee, EmployeeUpdate
from src.service.sample_manpower_list_service import SampleManpowerListService
from src.core.dependencies import get_sample_manpower_list_service

router = APIRouter()

@router.get("/api/v1/employees", response_model=List[Employee])
def view_employees(service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    return service.get_all()

@router.get("/api/v1/employees/csv")
def download_employees_csv_endpoint(response: Response, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    csv_data = service.export_to_csv()
    return StreamingResponse(StringIO(csv_data), media_type='text/csv', headers={"Content-Disposition": "attachment; filename=employees.csv"})

@router.get("/api/v1/employees/{manpower_id}", response_model=Employee)
def get_employee_detail(manpower_id: str, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    employee = service.get_employee_by_manpower_id(manpower_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.patch("/api/v1/employees/{manpower_id}", response_model=Employee)
def update_employee_endpoint(manpower_id: str, employee_update: EmployeeUpdate, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    db_employee = service.repository.get_by_manpower_id(manpower_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.update(db_employee, employee_update)

@router.post("/api/v1/employees", response_model=Employee)
def create_employee_endpoint(employee: EmployeeCreate, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    try:
        new_employee = service.create(employee)
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
