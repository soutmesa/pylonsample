from fastapi import FastAPI
from src.routes import sample_manpower_list_routes
from src.middleware.basic_auth_middleware import authenticate

app = FastAPI(
    title="Employee Management API with FastAPI",
    description="This API allows you to manage employee data, including creating, updating, and retrieving employee information, as well as exporting data to CSV.",
    version="1.0.0"
)

@app.middleware("http")
async def apply_auth_middleware(request, call_next):
    return await authenticate(request, call_next)

app.include_router(sample_manpower_list_routes.router, tags=["Employee"])
