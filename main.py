#Python
from argparse import OPTIONAL
from typing import Optional
#Pydantic
from pydantic import BaseModel
#FastApi
from fastapi import FastAPI, Query
from fastapi import Body, Query

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_maried: Optional[bool] = None


@app.get("/")
def home():
    return {"message": "Hello World"}

#request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

#Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[str] = Query(...) 
):
    return {name: age}