from fastapi import FastAPI
from databases import Profile

app = FastAPI()

@app.get('/')
def index():
    return "Hello World!!"

# query and path parameter simultaneously
@app.get('/profile/{userid}/comments')
def profile(userid:int, commentid:int):
    return {f'Profile page for user with user id {userid} and comment with {commentid}'}


# id here is a path parameter
@app.get('/property/{id}')
def property(id:int):
    return {"This is a property page {id}"}

# this static router, reaches first
@app.get('/movies/short')
def movies_series():
    return {'short movie list':{'Short Movie 1', 'Short Movie 2'}}

# this is a dynamic router
# username is path paramater 
@app.get('/movies/{username}')
def movies(username:str):
    return {'movie list':{'Movie 1', 'Movie 2'}}

@app.get('/movies')
def movies():
    return {'movie list':{'Movie 1', 'Movie 2'}}

# here id is a query parameter
# /products?id=10&price=200
@app.get('/products')
def products(id:int=1,price:int=10):
    return {f'products':{'id {id}', 'price {price}'}}

