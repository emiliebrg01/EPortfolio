from sqlmodel import Session
from repositories.repository import (create_person as create_person_repository, create_experience as create_experience_repository, create_formation as create_formation_repository, create_skill as create_skill_repository, create_book as create_book_repository)
from schemas.dto import PersonDTO, ExperienceDTO, FormationDTO, SkillsDTO


def create_person_service(session: Session, person_data: PersonDTO):
    return create_person_repository(session, person_data)


def create_experience_service(session: Session, experience_data: ExperienceDTO, person_id: int):
    return create_experience_repository(session, experience_data, person_id)


def create_formation_service(session: Session, formation_data: FormationDTO, person_id: int):
    return create_formation_repository(session, formation_data, person_id)


def create_skill_service(session: Session, skill_data: SkillsDTO, person_id: int):
    return create_skill_repository(session, skill_data, person_id)


def create_book_service(session: Session, photo: str, person_id: int):
    return create_book_repository(session, photo, person_id)



# A ajouter plus tard :

# email unique
# telephone unique
# etc ...
