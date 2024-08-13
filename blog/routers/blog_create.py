from urllib import request

from fastapi import APIRouter, status
from typing import List
from .. import schemas, models, oauth2
from ..database import get_db
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..database import get_db
from ..repository import blog_repository
from ..oauth2 import get_current_user  # Use relative import

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


get_db = database.get_db


# just changing from the @app to router bcz we have metnion the apirouter with refrence router
# getting all the blocks from the database
# we can define the tags inside the router , so that our code maximize
# as this code @router.post('/blog', status_code=status.HTTP_201_CREATED) ==
# > we can remove the ('/blog') from it blog and define it inside the router for proper and short code


@router.get('/', response_model=List[schemas.ShowBlog])  # here u have to mention the schemasblog with list, bcz u are fetching all the data u have to show it in the list if not list u got error
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).all()  as we define it into the repository of blog_repository.py to make more clean code
    return blog_repository.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return blog_repository.create(request, db)



@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.destroy(id, db)


# Know i am going to put or updating the data
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updating(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.update(id, request, db)


# Getting the data from db from blogs through the id
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)# we here decided the schema or data we want to show that like we only show here showblog fields only
def show(id: int, db: Session = Depends(get_db)):   # we can do this also def show(id, response: Response, db: Session = Depends(get_db)):
    return blog_repository.show(id, db)
