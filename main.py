#Python
from argparse import OPTIONAL
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel
from pydantic import Field
#FastApi
from fastapi import FastAPI, Query
from fastapi import Body, Query, Path

app = FastAPI()

#Models
class HairColor(Enum):
    brown = "brown"
    white = "white"
    black = 'black'
    blonde = 'blonde'
    red = 'red'


class Location(BaseModel):
    city: str
    state : str
    country : str

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        ge=0,
        le=150
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_maried: Optional[bool] = Field(default=None)


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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title = "Person Name",
        description="This is the person name. Its between 1 and 50 characters",
        ),
    age:Optional[str] = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required",
        )
):
    return {name: age}

#Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person id. It's required",
        )
):
    return {person_id: "It exists"}

#validaciones: request body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        title="Person ID",
        description="This is the person id. It's required",
        gt=0
        ),
    person: Person = Body(...),
    Location: Location = Body(...)
):
    results = person.dict(),
    results.update(Location.dict())
    return results