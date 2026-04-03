# ## Fichier main ##

# # Les classes à creer ! (chaque classe sera une partie du portfolio)

# # Classe personne (about me) : firstname, lastname, age, statut
# # Classe contact (mail, tel, linkdln, adress)
# #
# #
# # Classe expériences (name, year, place, skills, only (bool), status, )
# # Classe contact
# # Classe temoignage


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import create_engine, Session


#     def create_person():
#         return None

#     def get_person():
#         return None

#     def put_person():
#         return None

#     def delete_person():
#         return None


# class Contact:
#     def __init__(self, email, phone, linkdln, adress):
#         self.user_email = email
#         self.user_phone = phone
#         self.user_linkdln = linkdln
#         self.user_adress = adress


# class Project:
#     def __init__(self, name, year, place, skills, only, status):
#         self.project_name = name
#         self.project_year = year
#         self.project_place = place
#         self.project_skills = skills
#         self.project_only = only
#         self.project_status = status


# class testimonials:
#     def __init__():
#         return None


# Surement que methode CRUB elle sera gerer ailleurs

class Person:
    def __init__(self, firstname, lastname, age, status):
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_age = age
        self.statut = status

template = Jinja2Templates(directory="templates")

app = FastAPI()

name = "Maxence" # pas une liste mais une variable

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    context = {"name": name}
    return template.TemplateResponse(request, "template.html", context=context)


# Base de donnée 

sqlite_file_name = "database.db" # Nom de la base

sqlite_url = f"sqlite:///{sqlite_file_name}" # URL de connexion

engine = create_engine(    # 3. Création de engine -> connexion a la base de donnée
    sqlite_url,
    connect_args={"check_same_thread": False}  # obligatoire avec SQLite + FastAPI
)

def get_session():  # 4. Récupére la session
    with Session(engine) as session:
        yield session


# CRUD 
@app.post("/person/")
def create_person(person: Person, session: SessionDep):
    session.add(person)
    session.commit()
    session.refresh(person)
    return person

