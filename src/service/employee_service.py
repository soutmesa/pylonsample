from sqlalchemy import select, insert
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select
from sqlalchemy.engine import Result
import pandas as pd
import io
from ..models.employee import SampleManpowerList, EmployeeCreate

def get_employees(db: Session) -> List[Dict[str, Any]]:
    query: Select = select(SampleManpowerList)
    result: Result = db.execute(query)
    return [row._mapping for row in result]

def get_employee_by_manpower_id(db: Session, manpower_id: str):
    query = select(SampleManpowerList).where(SampleManpowerList.c.manpowerId == manpower_id)
    result = db.execute(query).first()
    if result is None:
        return None
    return dict(result._mapping)

def get_employee_by_id(db: Session, employee_id: int):
    query = select(SampleManpowerList).where(SampleManpowerList.c.id == employee_id)
    result = db.execute(query).first()
    if result is None:
        return None
    return dict(result._mapping)

def update_employee(db: Session, manpower_id: str, employee_data: EmployeeCreate):
    update_data = {k: v for k, v in employee_data.items() if v is not None}
    query = SampleManpowerList.update().where(SampleManpowerList.c.manpowerId == manpower_id).values(update_data)
    result = db.execute(query)
    if result.rowcount == 0:
        raise ValueError("Employee not found")
    db.commit()
    return get_employee_by_manpower_id(db, manpower_id)

def create_employee(db: Session, employee_data: EmployeeCreate):
    query = insert(SampleManpowerList).values(
        nric4Digit=employee_data.nric4Digit,
        name=employee_data.name,
        manpowerId=employee_data.manpowerId,
        designation=employee_data.designation,
        project=employee_data.project,
        team=employee_data.team,
        supervisor=employee_data.supervisor,
        joinDate=employee_data.joinDate,
        resignDate=employee_data.resignDate
    )
    result = db.execute(query)
    db.commit()
    employee_id = result.inserted_primary_key[0]
    return get_employee_by_id(db, employee_id)

def get_employees_csv(db: Session):
    employees = get_employees(db)
    df = pd.DataFrame(employees)
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return output.getvalue()
