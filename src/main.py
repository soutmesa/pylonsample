from fastapi import FastAPI
from src.routes import employee_route
from src.middleware.basic_auth_middleware import BasicAuthMiddleware

app = FastAPI()

app.include_router(employee_route.router, tags=["Employee"])
