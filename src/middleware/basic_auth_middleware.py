from fastapi import Request, HTTPException, Depends, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
from starlette.middleware.base import BaseHTTPMiddleware
from base64 import b64decode
import os

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Security setup
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})
    return True

class BasicAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, auth_dependency):
        super().__init__(app)
        self.auth_dependency = auth_dependency

    async def dispatch(self, request: Request, call_next):
        try:
            await self.auth_dependency()
        except HTTPException as e:
            return Response(content=e.detail, status_code=e.status_code, headers=e.headers)
        response = await call_next(request)
        return response