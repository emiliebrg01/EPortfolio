from sqlmodel import Session
from models.model import Person
from schemas.dto import PersonDTO
from models.model import User
from schemas.dto import UserRegisterDTO
from auth import hash_password
from sqlmodel import select


def create_person(session: Session, person_data: PersonDTO):
    person = Person(
        firstname=person_data.firstname,
        lastname=person_data.lastname,
        phone=person_data.phone,
        mail=person_data.mail,
    )
    session.add(person)
    session.commit()
    session.refresh(person)
    return person


def create_user(session: Session, user_data: UserRegisterDTO):
    hashed = hash_password(user_data.password)
    user = User(
        username=user_data.username, email=user_data.email, hashed_password=hashed
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_username(session: Session, username: str):
    return session.exec(select(User).where(User.username == username)).first()


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()
