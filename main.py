from fastapi import FastAPI
from pydantic import BaseModel


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

# @app.get('/blog')
# def blog(limit,  published: bool):
#     if published:
#         return {'data': f"{limit}  limit true from the url of google in ur path function operator"}
#     else:
#         return {'data': f"{limit} only the limit"}


# @app.get('/blog')
# def blog(limit):
#     return {'data': f"{limit}  limit from the url of google in ur path function operator"}

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


@app.post('/bloggers')
def create_blog():
    return {'data': 'Blog created by post'}













# @app.get('/')
# def index():
#     return 'simply the app decorator is running the index string'



# To open the templates and static files
# from fastapi import FastAPI, Request
# from typing import Union
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
#
# app = FastAPI()
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
#
# templates = Jinja2Templates(directory="templates")
#
#
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse('index.html', {'request': request})
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



# For simple understanding
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
#
# app = FastAPI()
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
#
# templates = Jinja2Templates(directory="templates")
#
#
# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )
