from fastapi import Depends, HTTPException, status
from .token import verify_token
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')  # this means our  token should be taken when we login


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},)

    return token.verify_token(data, credentials_exception=HTTPException)
