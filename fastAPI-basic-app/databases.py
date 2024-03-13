from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set

class Profile(BaseModel):
    name:str = Field(title='name of the person')
    email:str = Field(title='email')
    age:str = Field(title='age of the person')

class Image(BaseModel):
    url:HttpUrl
    name:str

class Product(BaseModel):
    name:str
    price:str
    discount:int
    discount_price:float
    tag:List[str] = []
    image:Image

class Offer(BaseModel):
    name:str
    description:str
    price:float
    products:List[Product]