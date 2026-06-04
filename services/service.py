from sqlmodel import Session
from repositories.repository import create_person as create_person_repository
from schemas.dto import PersonDTO
from repositories.repository import create_user, get_user_by_username, get_user_by_email
from schemas.dto import UserRegisterDTO, UserLoginDTO
from auth import verify_password


def create_person_service(session: Session, person_data: PersonDTO):
    return create_person_repository(session, person_data)


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
