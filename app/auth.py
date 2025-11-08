import os
import secrets
from typing import Optional
from fastapi import HTTPException, status, Depends, Cookie
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
from app.config import settings 

# security = HTTPBasic()
_signer = TimestampSigner(settings.session_secret)

def _create_session_token(username: str) -> str:
    return _signer.sign(username.encode()).decode()

def _verify_session_token(token:str) -> str:
    try:
        raw = _signer.unsign(token, max_age=settings.session_max_age)
        return raw.decode()
    except (BadSignature, SignatureExpired):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token"
        )

def get_current_user_cookie(session: Optional[str]= Cookie(None, alias=settings.session_cookie_name)):
    if not session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No session")
    return _verify_session_token(session)

def verify_user_password(username:str, password:str) -> bool:
    expected = settings.basic_users.get(username)
    return expected is not None and secrets.compare_digest(expected, password)


# def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
#     expected = settings.basic_users.get(credentials.username)
#     ok = expected is not None and secrets.compare_digest(expected, credentials.password)
#     if not ok:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Unauthorized",
#             headers={"WWW-Authenticate": "Basic"},    
#         )
#     return credentials.username