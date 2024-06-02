import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.connection import Base, get_db_session

# Configure test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_session] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield client
    Base.metadata.drop_all(bind=engine)

def test_create_employee(test_client):
    response = test_client.post(
        "/api/v1/employees",
        json={
            "nric4Digit": "7890",
            "name": "Emily Davis",
            "manpowerId": "EMP125",
            "designation": "Data Analyst",
            "project": "Project D",
            "team": "Team W",
            "supervisor": "Clark Kent",
            "joinDate": "2024-03-15",
            "resignDate": None
        },
        auth=("username", "password")
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Emily Davis"

def test_view_employees(test_client):
    response = test_client.get("/api/v1/employees", auth=("username", "password"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_employee_detail(test_client):
    response = test_client.get("/api/v1/employees/EMP125", auth=("username", "password"))
    assert response.status_code == 200
    assert response.json()["manpowerId"] == "EMP125"

def test_update_employee(test_client):
    response = test_client.patch(
        "/api/v1/employees/EMP125",
        json={
            "designation": "Senior Data Analyst",
            "project": "Project E",
            "team": "Team X",
            "supervisor": "Bruce Wayne",
            "joinDate": "2024-03-15",
            "resignDate": None
        },
        auth=("username", "password")
    )
    assert response.status_code == 200
    assert response.json()["designation"] == "Senior Data Analyst"

def test_download_employees_csv(test_client):
    response = test_client.get("/api/v1/employees/csv", auth=("username", "password"))
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment; filename=employees.csv"
    assert response.headers["Content-Type"] == "text/csv"
