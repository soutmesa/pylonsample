from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from .connection import get_db_session
from src.repository.sample_manpower_list_repository import SampleManpowerListRepository
from src.service.sample_manpower_list_service import SampleManpowerListService

load_dotenv()

security = HTTPBasic()

def get_sample_manpower_list_service(db: Session = Depends(get_db_session)):
    repository = SampleManpowerListRepository(db)
    service = SampleManpowerListService(repository)
    return service

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True
