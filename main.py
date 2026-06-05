# ## Fichier main ##

#################
#### IMPORTS ####
#################
from datetime import date

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlmodel import Session, SQLModel

from database import engine
from models import model

from schemas.dto import PersonDTO, ExperienceDTO, FormationDTO,SkillsDTO, BookDTO

from services.service import (create_person_service, create_experience_service, create_formation_service, create_skill_service, create_book_service)

# Initialisation FastAPI 
app = FastAPI()
template = Jinja2Templates(directory="templates")
app.mount("/styles", StaticFiles(directory="styles"), name="styles") # lie l'url "/styles" au dossier local styles


# Creation des bases de données au demarrage
SQLModel.metadata.create_all(engine)


# Routers
@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return template.TemplateResponse(
        request, 
        "form.html",
        context={"request": request}
    )

@app.post("/generate", response_class=HTMLResponse)
async def generate_port(request: Request):

    data_form = await request.form() # recupere les données envoyées par le formulaire HTML

    # Récupere les champs simple du formulaire
    firstname = data_form.get("firstname", "")
    lastname = data_form.get("lastname", "")
    mail = data_form.get("mail", "")
    phone = data_form.get("phone", "")
    linkedin = data_form.get("linkedin", "")

    # Création de listes pour stocker les experiences, informations, skills
    experiences = []
    formations = []
    skills = []
    books = []

    # Création de set pour reperer les indexes et éviter les doublons 
    exp = set()
    form = set()
    sk = set()
    bk = set()

    # Repere les indexs
    for key in data_form.keys():
        if key.startswith("job_"):
            exp.add(key.split("_")[1])

        if key.startswith("formation_"):
            form.add(key.split("_")[1])

        if key.startswith("name_"):
            sk.add(key.split("_")[1])

        if key.startswith("photo_"):
            bk.add(key.split("_")[1])

    # Reconstruit les experiences 
    for index in sorted(exp, key=int):
        experiences.append(
        {
            "job": data_form.get(f"job_{index}", ""),
            "company" : data_form.get(f"company_{index}", ""),
            "start" : data_form.get(f"exp_start_{index}", ""),
            "end" : data_form.get(f"exp_end_{index}", ""),
            "description" : data_form.get(f"exp_desc_{index}", ""),
        }
        )

    # Reconstruits les formations
    for index in sorted(form, key=int):
        formations.append(
        {
            "formation" : data_form.get(f"formation_{index}", ""),
            "university" : data_form.get(f"university_{index}", ""),
            "start" : data_form.get(f"form_start_{index}", ""),
            "end" : data_form.get(f"form_end_{index}", ""),
            "description" : data_form.get(f"form_desc_{index}", ""),
        }
        )

    # Reconstruit les skills
    for index in sorted(sk, key=int):
        skills.append(
        {
            "name" : data_form.get(f"name_{index}", ""),
            "level" : data_form.get(f"level_{index}", ""),
        }
        )

    # Reconstruire les book
    for index in sorted(bk, key=int):
        books.append(
        {
            "photo" : data_form.get(f"photo_{index}", ""),
        }
        )

    # Appel du service pour enregistrement en base de données
    with Session(engine) as session:
        person_dto = PersonDTO(
        firstname = firstname,
        lastname = lastname,
        mail = mail,
        phone = phone,
        linkedin = linkedin,
        )
    
    person = create_person_service(session, person_dto)


    for exp_item in experiences:
        experience_dto = ExperienceDTO(
            job_name = exp_item["job"],
                company_name = exp_item["company"],
                date_start = date.fromisoformat(exp_item["start"]) if exp_item["start"] else None,
                date_end = date.fromisoformat(exp_item["end"]) if exp_item["end"] else None,
                contract_type = "",
                description = exp_item["description"],
            )
        
        create_experience_service(session, experience_dto, person.id)

    
    for form_item in formations:
        formation_dto = FormationDTO(
            name = form_item["formation"],
            date_start = date.fromisoformat(form_item["start"]) if form_item["start"] else None,
            date_end = date.fromisoformat(form_item["end"]) if form_item["end"] else None,
            secteur = form_item["university"],
            degree_type = "",
            description = form_item["description"],
            )
        
        create_formation_service(session, formation_dto, person.id)
    

    for skill_item in skills:
        skill_dto = SkillsDTO(
            name = skill_item["name"],
            level = int(skill_item["level"]) if skill_item["level"] else 0,
        )

        create_skill_service(session, skill_dto, person.id)


    for book_item in books:
        book_dto = BookDTO(
            photo = book_item["photo"]
        )

        create_book_service(session, book_dto, person.id)

    context = {
        "request" : request,
        "firstname": firstname,
        "lastname": lastname,
        "mail": mail,
        "phone": phone,
        "linkedin": linkedin,
        "experiences" : experiences,
        "formations" : formations,
        "skills": skills,
        "books": books
    }

    return template.TemplateResponse(
        request,
        "Template.html",
        context=context
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
