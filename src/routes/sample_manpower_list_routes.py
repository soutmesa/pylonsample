from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import StreamingResponse
from io import StringIO
from typing import List
from src.schema.sample_manpower_list_schema import EmployeeCreate, Employee, EmployeeUpdate
from src.service.sample_manpower_list_service import SampleManpowerListService
from src.core.dependencies import get_sample_manpower_list_service, authenticate

router = APIRouter()

@router.get("/api/v1/employees", response_model=List[Employee], dependencies=[Depends(authenticate)])
def view_employees(service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    """
    Retrieve all employees.

    This endpoint retrieves all employee data from the SampleManpowerList table, including their ID, name, designation, project, team, supervisor, join date, and resign date if applicable.
    """
    return service.get_all()

@router.get("/api/v1/employees/csv", dependencies=[Depends(authenticate)])
def download_employees_csv_endpoint(response: Response, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    """
    Download employee data as CSV.

    This endpoint allows you to download all employee data from the SampleManpowerList table in CSV format. This includes all the relevant fields for each employee.
    """
    csv_data = service.export_to_csv()
    return StreamingResponse(StringIO(csv_data), media_type='text/csv', headers={"Content-Disposition": "attachment; filename=employees.csv"})

# @router.get("/api/v1/employees/{manpower_id}", response_model=Employee, dependencies=[Depends(authenticate)])
# def get_employee_detail(manpower_id: str, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
#     """
#     Retrieve an employee by manpower_id.

#     This endpoint retrieves an employee data from the SampleManpowerList table, including their ID, name, designation, project, team, supervisor, join date, and resign date if applicable.
#     """
#     employee = service.get_employee_by_manpower_id(manpower_id)
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

@router.patch("/api/v1/employees/{manpower_id}", response_model=Employee, dependencies=[Depends(authenticate)])
def update_employee_endpoint(manpower_id: str, employee_update: EmployeeUpdate, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
    """
    Update employee details.

    This endpoint allows you to update specific details of an employee such as their designation, project, team, supervisor, join date, and resign date using their unique manpowerId.
    
    - **manpowerId**: The unique identifier of the employee to be updated.
    - **employee_update**: A JSON object containing the details to be updated.
    
    Example request body:
    ```
    {
        "designation": "New Designation",
        "project": "New Project",
        "team": "New Team",
        "supervisor": "New Supervisor",
        "joinDate": "2024-01-01",
        "resignDate": "2024-12-31"
    }
    ```
    """
    db_employee = service.repository.get_by_manpower_id(manpower_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return service.update(db_employee, employee_update)

# @router.post("/api/v1/employees", response_model=Employee, dependencies=[Depends(authenticate)])
# def create_employee_endpoint(employee: EmployeeCreate, service: SampleManpowerListService = Depends(get_sample_manpower_list_service)):
#     """
#     Create a new employee.

#     This endpoint allows you to create a new employee record in the SampleManpowerList table.
    
#     - **nric4Digit**: The last 4 digits of the Employee's IC number.
#     - **name**: The name of the employee.
#     - **manpowerId**: The unique manpower ID of the employee.
#     - **designation**: The job title of the employee.
#     - **project**: The current project assigned to the employee.
#     - **team**: The team within the organization the employee belongs to.
#     - **supervisor**: The name of the supervisor responsible for the employee.
#     - **joinDate**: The date the employee joined the company (format: YYYY-MM-DD).
#     - **resignDate**: The date the employee left the company, if applicable (format: YYYY-MM-DD).
    
#     Example request body:
#     ```
#     {
#         "nric4Digit": "1234",
#         "name": "John Doe",
#         "manpowerId": "EMP001",
#         "designation": "Software Engineer",
#         "project": "Project Alpha",
#         "team": "Development",
#         "supervisor": "Jane Smith",
#         "joinDate": "2023-01-01",
#         "resignDate": null
#     }
#     ```
#     """
#     try:
#         new_employee = service.create(employee)
#         return new_employee
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
