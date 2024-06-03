from sqlalchemy.orm import Session
from src.models.sample_manpower_list_model import SampleManpowerList
from src.repository.base_repository import BaseRepository

class SampleManpowerListRepository(BaseRepository[SampleManpowerList]):
    def __init__(self, db: Session):
        super().__init__(SampleManpowerList, db)

    def get_by_manpower_id(self, manpower_id: str):
        return self.db.query(self.model).filter(self.model.manpowerId == manpower_id).first()