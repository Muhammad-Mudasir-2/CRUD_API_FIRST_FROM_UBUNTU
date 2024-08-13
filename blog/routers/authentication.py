from http.client import HTTPException
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException
from fastapi import APIRouter, Depends
from .. import schemas
from .. import database
from sqlalchemy.orm import Session
from .. import models, token
from ..hashing import Hash
from datetime import timezone, timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found. Invalid credentials.")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password. Invalid credentials.")

    access_token = token.create_access_token( data={"sub": user.email})
    return {"access_token":access_token, "token_type": "bearer"}

## means that the user.password is the user which the user created in the docs and official
# note the user password was in the form of hashed password bcz due  to the hashing.py
# and the request.password means when someone try to to login with  a password so in both cases we have to verify both
