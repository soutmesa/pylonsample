from fastapi import FastAPI
from .routes import employees

app = FastAPI()

app.include_router(employees.router, tags=["employee"])
