
from fastapi import FastAPI, Request, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import schemas, models, hashing
from typing import List
from .schemas import User, ShowUser, ShowBlog
import hashlib
from passlib.context import CryptContext
from .hashing import Hash
from .database import Base, engine
from .routers import blog_create, user, authentication

app = FastAPI()

#  we done when we have to remove the data from the db the error fo sqlalchemy we got
# models.Base.metadata.create_all(engine)
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


# just putting it into the database.py for more accurate and precise way
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# know i am telling that from app just take the proper route for the api path,
# mean that the router path is crated in router.blog_create.py just u have to tell or include this path
app.include_router(blog_create.router)
app.include_router(user.router)

app.include_router(authentication.router)

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# To delete from the db


# @app.post('/blog', status_code=201)
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# # Know i am going to put or updating the data
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def updating(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     # db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())  # From the ui to update the things
#     # db.query(models.Blog).filter(models.Blog.id == id).update({'title': "updatd title"})  from coding to update
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():   # we are doing this secure if the id is not exist raise and if id exist so take reqeuest and edit
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} u want to see "
#                                                                           "is not found ")
#     blog.update(request.dict())
#     db.commit()
#     return "Updated"


# putting this intot the router for accurate strucutre
# # getting all the blocks from the database
# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])  # here u have to mention the schemasblog with list, bcz u are fetching all the data u have to show it in the list if not list u got error
# def all_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# # Getting the data from db from blogs through the id
# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs']) # we here decided the schema or data we want to show that like we only show here showblog fields only
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()   # To check the data, from the id with exception status if the data is not crated and the status code should show the not found instead of the null
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"blog with this id{id} isnt found and checked with exception status")
#     return blog

# # Getting the data from db from blogs through the id
# @app.get('/blog/{id}', status_code=200)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()   # To check the data, from the id with status if the data is not crated and the status code should show the not found instead of the null
#     if not blog:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"details": f"Blog with this id {id} is not found and not created"}
#     return blog


# # Getting the data from db from blogs through the id
# @app.get('/blog/{id}')
# def get_blog_id(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     return blog



# from fastapi import FastAPI
#
#
# app = FastAPI()
#
#
# @app.post('/blog')
# def create(title, body):
#     return {'title':title, 'body':body}
#
#


# @app.post('/user', response_model=schemas.ShowUser, tags=['USERS'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['USERS'])
# def get_user(id:int, db:Session = Depends(get_db)):
#     all_users = db.query(models.User).filter(models.User.id==id).first()
#     if not all_users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with this id {id} is not available")
#
#     return all_users

