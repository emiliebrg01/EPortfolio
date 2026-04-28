from sqlmodel import Session
from models.person_model import Person
from schemas.person_dto import PersonDTO

def create_person(session:Session, person_data:PersonDTO):
    person = Person(
        firstname = person_data.firstname,
        lastname = person_data.lastname,
        phone = person_data.phone,
        mail = person_data.mail 
    )

    session.add(person)
    session.commit()
    session.refresh(person)

    return person

