from sqlmodel import Session
from repositories.person_repository import create_person as create_person_repository
from schemas.person_dto import PersonDTO

def create_person_service(session:Session, person_data:PersonDTO):
    return create_person_repository(session, person_data)

# A ajouter plus tard : 

# email unique 
# telephone unique 
# etc ...


