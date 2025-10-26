import os
import secrets
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.config import settings 

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    expected = settings.basic_users.get(credentials.username)
    ok = expected is not None and secrets.compare_digest(expected, credentials.password)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},    
        )
    return credentials.username