from fastapi import APIRouter, status
from typing import List
from .. import schemas, models
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..database import get_db
from ..hashing import Hash
from ..repository import user_repository


router = APIRouter(
    prefix="/user",
    tags=['users']
)


get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user_repository.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user_repository.show_user(id, db)
