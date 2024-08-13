from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def intro():
    return {'data': {
        'name': "Mudasir",
        'age': 19
    }}


@app.get('/blog/{id}')
def rank():
    return {'data': {
        'name': 'IBM',
        'rank': 1
    }}
