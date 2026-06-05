from sqlmodel import Session
from repositories.repository import (create_person as create_person_repository, create_experience as create_experience_repository, create_formation as create_formation_repository, create_skill as create_skill_repository, create_book as create_book_repository, create_user, get_user_by_username, get_user_by_email)
from schemas.dto import PersonDTO, ExperienceDTO, FormationDTO, SkillsDTO, UserRegisterDTO, UserLoginDTO
from auth import verify_password


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

def register_user(session: Session, user_data: UserRegisterDTO):
    if get_user_by_username(session, user_data.username):
        return None, "Nom d'utilisateur déjà pris"
    if get_user_by_email(session, user_data.email):
        return None, "Email déjà utilisé"
    return create_user(session, user_data), None


def login_user(session: Session, user_data: UserLoginDTO):
    user = get_user_by_username(session, user_data.username)
    if not user:
        return None
    if not verify_password(user_data.password, user.hashed_password):
        return None
    return user


# A ajouter plus tard :

# email unique
# telephone unique
# etc ...
