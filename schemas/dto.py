from sqlmodel import SQLModel
from datetime import date

class PersonBaseDTO(SQLModel):
    firstname: str
    lastname: str
    phone: str
    mail: str


class PersonDTO(PersonBaseDTO):
    pass


class PersonResponseDTO(PersonBaseDTO):
    id: int


class UserRegisterDTO(SQLModel):
    username: str
    email: str
    password: str


class UserLoginDTO(SQLModel):
    username: str
    password: str
class ExperienceBaseDTO(SQLModel):
    job_name: str
    company_name: str
    date_start: date
    date_end: date
    contract_type: str = ""
    description: str = ""

class ExperienceDTO(ExperienceBaseDTO):
    pass


class ExperienceResponseDTO(ExperienceBaseDTO):
    id: int

class FormationBaseDTO(SQLModel):
    name: str
    date_start: date
    date_end: date
    secteur: str = ""
    degree_type: str = ""
    description: str = ""

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

