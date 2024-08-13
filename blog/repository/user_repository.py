from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_user(id: int, db: Session):
    all_users = db.query(models.User).filter(models.User.id==id).first()
    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with this id {id} is not available")

    return all_users
