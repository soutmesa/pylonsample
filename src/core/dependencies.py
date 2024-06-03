from fastapi import Depends
from sqlalchemy.orm import Session
from .connection import get_db_session
from src.repository.sample_manpower_list_repository import SampleManpowerListRepository
from src.service.sample_manpower_list_service import SampleManpowerListService

def get_sample_manpower_list_service(db: Session = Depends(get_db_session)):
    repository = SampleManpowerListRepository(db)
    service = SampleManpowerListService(repository)
    return service
