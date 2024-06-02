from typing import List, Dict, Any
import pandas as pd
import io
from sqlalchemy.orm import Session
from src.repository.employee_repository import EmployeeRepository
from src.models.employee import EmployeeCreate

class EmployeeService:
    def __init__(self, db: Session):
        self.repository = EmployeeRepository(db)

    def get_employees(self) -> List[Dict[str, Any]]:
        return self.repository.get_all()

    def get_employee_by_manpower_id(self, manpower_id: str):
        return self.repository.get_by_manpower_id(manpower_id)

    def update_employee(self, manpower_id: str, employee_data: Dict[str, Any]):
        return self.repository.update(manpower_id, employee_data)

    def create_employee(self, employee_data: EmployeeCreate):
        return self.repository.create(employee_data)

    def get_employees_csv(self):
        employees = self.repository.get_all()
        df = pd.DataFrame(employees)
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return output.getvalue()
