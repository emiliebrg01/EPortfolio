from sqlmodel import Session
from models.model import Person, Experience, Formation, Skills, Book
from schemas.dto import PersonDTO, ExperienceDTO, FormationDTO, SkillsDTO


def create_person(session: Session, person_data: PersonDTO):
    person = Person(
        firstname = person_data.firstname,
        lastname = person_data.lastname,
        phone = person_data.phone,
        mail = person_data.mail,
    )

    session.add(person)
    session.commit()
    session.refresh(person)

    return person

def create_experience(session: Session, experience_data: ExperienceDTO, person_id: int):
    experience = Experience(
        job_name = experience_data.job_name,
        company_name = experience_data.company_name,
        date_start = experience_data.date_start,
        date_end = experience_data.date_end,
        contract_type = experience_data.contract_type,
        description = experience_data.description,
        person_id = person_id,
    )

    session.add(experience)
    session.commit()
    session.refresh(experience)

    return experience


def create_formation(session: Session, formation_data: FormationDTO, person_id: int):
    formation = Formation(
        name = formation_data.name,
        date_start = formation_data.date_start,
        date_end = formation_data.date_end,
        secteur = formation_data.secteur,
        degree_type = formation_data.degree_type,
        description = formation_data.description,
        person_id = person_id,
    )

    session.add(formation)
    session.commit()
    session.refresh(formation)

    return formation


def create_skill(session: Session, skill_data: SkillsDTO, person_id: int):
    skill = Skills(
        name = skill_data.name,
        level = skill_data.level,
        person_id = person_id,
    )

    session.add(skill)
    session.commit()
    session.refresh(skill)

    return skill


def create_book(session: Session, photo: str, person_id: int):
    book = Book(
        photo = photo,
        person_id = person_id,
    )

    session.add(book)
    session.commit()
    session.refresh(book)

    return book
