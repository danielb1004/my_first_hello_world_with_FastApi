#Python
from argparse import OPTIONAL
from typing import Optional
#Pydantic
from pydantic import BaseModel
#FastApi
from fastapi import FastAPI
from fastapi import Body

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