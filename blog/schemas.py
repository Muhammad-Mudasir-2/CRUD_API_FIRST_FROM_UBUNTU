from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional


class BaseBlog(BaseModel):
    title: str
    body: str


class Blog(BaseBlog):
    class Config():
        from_attributes = True

# bcz we only want to show those fields which we want to show them , means to restrict to a speicfic
# model fields we want to show


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []        # here we are trying to list all the blocks
    class Config:
        from_attributes = True


class ShowBlog(BaseModel):  # Know we only restrict to showblog fields which we want to show
    title: str
    body: str
    creator: ShowUser

    class Config:
        from_attributes = True  # We can write it as == orm_mode = True


class Login(BaseModel):
    username: str
    password: str


# from the docs code of jwt
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None






#
# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from typing import List
#
#
# class Blog(BaseModel):
#     title: str
#     body: str
#
#
# # bcz we only want to show those fields which we want to show them , means to restrict to a speicfic
# # model fields we want to show
#
#
# class User(BaseModel):
#     name: str
#     email: str
#     password: str
#
#
# class ShowUser(BaseModel):
#     name: str
#     email: str
#
#     class Config:
#         from_attributes = True
#
#
# class ShowBlog(BaseModel):  # Know we only restrict to showblog fields which we want to show
#     title: str
#     body: str
#     creator: ShowUser
#
#     class Config:
#         from_attributes = True  # We can write it as == orm_mode = True
