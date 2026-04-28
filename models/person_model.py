from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class Person (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    phone: str
    mail: str
    linkedln : str


class Experience (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    job_name : str
    company_name : str
    date_start : date
    date_end : date
    type : str
    description : str
    id : int = Field(foreign_key="Person.id")


class Skills (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    level : int
    id: int = Field(foreign_key="Person.id")

class Formation (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    date_start : date
    date_end : date
    secteur : str
    type : str
    person : int = Field(foreign_key="person.id")

class Book (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    photo : str
    number : int 
    person : int = Field(foreign_key="Person.id")
