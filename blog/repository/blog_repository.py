from urllib.request import Request
from sqlalchemy.orm import Session
from ..import models, schemas
from ..models import Blog
from ..import schemas
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException


# here we are definiing only the method or repository where u can do the functionality of a code
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(ilanguaged:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} u want to see and delete"
                                                                          "is not found ")
    blog.delete(synchronize_session=False)
    db.commit()  # Bcz when we do some changes in db we have to db.commit for proper functioning or changes
    return {'The deletion has been done'}


def update(id:int, request: schemas.Blog, db: Session):
    # db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())  # From the ui to update the things
    # db.query(models.Blog).filter(models.Blog.id == id).update({'title': "updatd title"})  from coding to update
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():   # we are doing this secure if the id is not exist raise and if id exist so take reqeuest and edit
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} u want to see "
                                                                          "is not found ")
    blog.update(request.dict())
    db.commit()
    return "Updated"


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()   # To check the data, from the id with exception status if the data is not crated and the status code should show the not found instead of the null
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with this id{id} isnt found and checked with exception status")
    return blog
