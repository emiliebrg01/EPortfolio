from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    phone: str
    mail: str
    linkedin: str = ""


class Experience(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_name: str
    company_name: str
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    contract_type: str = ""
    description: str = ""
    person_id: int = Field(foreign_key="person.id")


class Skills(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    level: int
    person_id: int = Field(foreign_key="person.id")


class Formation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    secteur: str = ""
    degree_type: str = ""
    description: str = ""
    person_id: int = Field(foreign_key="person.id")


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    photo: str
    person_id: int = Field(foreign_key="person.id")
