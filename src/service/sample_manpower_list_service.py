import pandas as pd
import io
from src.repository.sample_manpower_list_repository import SampleManpowerListRepository
from src.service.base_service import BaseService
from src.models.sample_manpower_list_model import SampleManpowerList

class SampleManpowerListService(BaseService[SampleManpowerList, SampleManpowerListRepository]):
    def __init__(self, repository: SampleManpowerListRepository):
        super().__init__(repository)

    def get_employee_by_manpower_id(self, manpower_id: str):
        return self.repository.get_by_manpower_id(manpower_id)
    
    def export_to_csv(self):
        employees = self.repository.get_all()
        
        # Convert Employee objects to dictionaries
        employee_dicts = []
        for employee in employees:
            employee_dict = {
                "id": employee.id,
                "nric4Digit": employee.nric4Digit,
                "name": employee.name,
                "manpowerId": employee.manpowerId,
                "designation": employee.designation,
                "project": employee.project,
                "team": employee.team,
                "supervisor": employee.supervisor,
                "joinDate": employee.joinDate,
                "resignDate": employee.resignDate
            }
            employee_dicts.append(employee_dict)

        # Create DataFrame from list of dictionaries
        df = pd.DataFrame(employee_dicts)
        
        # Convert DataFrame to CSV string
        csv_data = df.to_csv(index=False)
        return csv_data