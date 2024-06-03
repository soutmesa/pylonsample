from fastapi import Response
from fastapi.security import HTTPBasic
import os, base64

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

security = HTTPBasic()

async def authenticate(request, call_next):
    try:
        auth = request.headers["Authorization"]
        scheme, credentials = auth.split()
        assert scheme.lower() == "basic"
        username, password = base64.b64decode(credentials).decode().split(":")
        if username == USERNAME and password == PASSWORD:
            response = await call_next(request)
        else:
            response = Response(
                "Unauthorized",
                status_code=401,
                headers={"WWW-Authenticate": "Basic"},
            )
    except KeyError:
        response = Response(
            "Unauthorized",
            status_code=401,
            headers={"WWW-Authenticate": "Basic"},
        )
    except Exception as e:
        response = Response(
            "Internal Server Error",
            status_code=500
        )
    return response