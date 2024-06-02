from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update
from src.models.employee import SampleManpowerList, EmployeeCreate

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        query = select(SampleManpowerList)
        result = self.db.execute(query)
        return [row._mapping for row in result]

    def get_by_manpower_id(self, manpower_id: str):
        query = select(SampleManpowerList).where(SampleManpowerList.c.manpowerId == manpower_id)
        result = self.db.execute(query).first()
        return dict(result._mapping) if result else None

    def get_by_id(self, employee_id: int):
        query = select(SampleManpowerList).where(SampleManpowerList.c.id == employee_id)
        result = self.db.execute(query).first()
        return dict(result._mapping) if result else None

    def create(self, employee_data: EmployeeCreate):
        query = insert(SampleManpowerList).values(**employee_data.dict())
        result = self.db.execute(query)
        self.db.commit()
        return self.get_by_id(result.inserted_primary_key[0])

    def update(self, manpower_id: str, employee_data: dict):
        query = update(SampleManpowerList).where(SampleManpowerList.c.manpowerId == manpower_id).values(**employee_data)
        self.db.execute(query)
        self.db.commit()
        return self.get_by_manpower_id(manpower_id)
