from fastapi import FastAPI
from src.routes import sample_manpower_list_routes
from src.middleware.basic_auth_middleware import authenticate

app = FastAPI()

@app.middleware("http")
async def apply_auth_middleware(request, call_next):
    return await authenticate(request, call_next)

app.include_router(sample_manpower_list_routes.router, tags=["Employee"])
