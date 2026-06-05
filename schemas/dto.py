from sqlmodel import SQLModel
from datetime import date

from typing import Optional


class PersonBaseDTO(SQLModel):
    firstname: str
    lastname: str
    phone: str
    mail: str
    linkedin : str

class PersonDTO(PersonBaseDTO):
    pass

class PersonResponseDTO(PersonBaseDTO):
    id: int


class ExperienceBaseDTO(SQLModel):
    job_name: str
    company_name: str
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    contract_type: str
    description: str

class ExperienceDTO(ExperienceBaseDTO):
    pass

class ExperienceResponseDTO(ExperienceBaseDTO):
    id: int


class FormationBaseDTO(SQLModel):
    name: str
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    secteur: str 
    degree_type: str 
    description: str 

class FormationDTO(FormationBaseDTO):
    pass

class FormationREsponseDTO(FormationBaseDTO):
    id: int


class SkillsBaseDTO(SQLModel):
    name: str
    level: int

class SkillsDTO(SkillsBaseDTO):
    pass

class SkilsResponseDTO(SkillsBaseDTO):
    id: int


class BookBaseDTO(SQLModel):
    name: str
    level: int

class BookDTO(BookBaseDTO):
    pass

class BookResponseDTO(BookBaseDTO):
    id: int

