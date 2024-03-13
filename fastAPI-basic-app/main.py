from fastapi import FastAPI
from databases import Profile, Product, Offer

app = FastAPI()

@app.get('/')
def index():
    return "Hello World!!"

@app.get('/profile/{userid}/comments')
def profile(userid:int, commentid:int):
    return {f'Profile page for user with user id {userid} and comment with {commentid}'}

@app.post('/adduser')
def adduser(profile:Profile, age:int):
    return {'user data':profile}

@app.post('/addproduct/{product_id}/')
def addproduct(product:Product, product_id:int):
    product.discount_price = product.price - (product.price * product.discount)/100
    return {'product data':product}

@app.post('/addoffer')
def addoffer(offer:Offer):
    return {offer}