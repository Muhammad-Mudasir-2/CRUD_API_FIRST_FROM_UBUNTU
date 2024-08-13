
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn

import main_2

app = FastAPI()


@app.get('/')  # this is the base or main path
def index():  # -----------------
    return {'data': {    # ----------------- path operation function
        'name': 'Mudasi'    # -----------------
    }}


@app.get('/blog')
def blog(limit=10,  published: bool = True):
    if published:
        return {'data': f"{limit}  limit true from the url of google in ur path function operator"}
    else:
        return {'data': f"{limit} only the limit"}


@app.get('/about')
def about():
    return {'data': {
        'name': 'Taking Mudasir name from the about route'
    }}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished data is here.'}


@app.get('/show_ids/{id}')
def show(id: int):   # specifying that the id must be int
    return {'data': {id}}


@app.get('/show_ids/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    body: str
    title: str
    published_at: Optional[bool]


@app.post('/bloggers')
def create_blog(request: Blog):  # u may write it as def create_blog(blog: Blog)
    return {'data': f"Blog created by post with the title of {request.title} with body{request.body}"}

# @app.post('/bloggers')
# def create_blog(request: Blog):  # u may write it as def create_blog(blog: Blog)
#     return {'data': 'Blog created by post'}

# To change the port with the uvcorn
if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=9000)
