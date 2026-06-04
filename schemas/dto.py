from sqlmodel import SQLModel


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
