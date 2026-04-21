from sqlmodel import SQLModel, Field
from typing import Optional


class Person (SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    phone: str
    mail: str