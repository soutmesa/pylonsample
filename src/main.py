from fastapi import FastAPI, Depends, Response
from .database.database import get_db_session, get_employees, update_employee, get_employees_csv
from .auth.auth import authenticate
from sqlalchemy.orm import Session
import pandas as pd
from typing import List, Dict, Any

app = FastAPI()

@app.get("/api/v1/employees", response_model=List[Dict[str, Any]])
def view_employees(db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    return [dict(row) for row in get_employees(db)]

@app.patch("/api/v1/employees/{manpower_id}")
def update_employee_endpoint(manpower_id: str, employee_data: dict, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    return update_employee(db, manpower_id, employee_data)

@app.get("/api/v1/employees/csv")
def download_employees_csv_endpoint(response: Response, db: Session = Depends(get_db_session), authorized: bool = Depends(authenticate)):
    csv_data = get_employees_csv(db)
    response.headers["Content-Disposition"] = "attachment; filename=employees.csv"
    return Response(content=csv_data, media_type="text/csv")
