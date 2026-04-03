# ## Fichier main ##

#################
#### IMPORTS ####
#################
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import create_engine, Session
from typing import Annotated

################################
#### Initialisation FastAPI ####
################################
app = FastAPI()
template = Jinja2Templates(directory="templates")

########################
#### Base de donnée ####
########################

sqlite_file_name = "database.db" # Nom de la base

sqlite_url = f"sqlite:///{sqlite_file_name}" # URL de connexion

engine = create_engine(    # 3. Création de engine -> connexion a la base de donnée
    sqlite_url,
    connect_args={"check_same_thread": False}  # obligatoire avec SQLite + FastAPI
)

def get_session():  # 4. Récupére la session
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

######################
#### Model Person ####
######################

class Person:
    def __init__(self, firstname, lastname, age, status):
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_age = age
        self.statut = status



'''
firtsname = "Maxence"
name = "Baissas"
phone = "0615154270"
mail = "maxence.baissas@epfedu.fr"
experiences = []
formations = []


@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    context = {
        "name": name,
        "firstname": firtsname,
        "phone": phone,
        "mail": mail,
        "experiences": experiences,
        "formations": formations,
    }
    return template.TemplateResponse(request, "template.html", context=context)
'''

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return template.TemplateResponse("form.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate_cv(request: Request):
    form = await request.form()

    data = {
        "prenom": form.get("prenom"),
        "nom": form.get("nom"),
        "email": form.get("email"),
        "telephone": form.get("telephone"),
        "experiences": [],
        "formations": []
    }

    # Expériences
    i = 0
    while form.get(f"poste_{i}"):
        data["experiences"].append({
            "poste": form.get(f"poste_{i}"),
            "entreprise": form.get(f"entreprise_{i}"),
            "debut": form.get(f"exp_debut_{i}"),
            "fin": form.get(f"exp_fin_{i}"),
            "description": form.get(f"exp_desc_{i}")
        })
        i += 1

    # Formations
    i = 0
    while form.get(f"diplome_{i}"):
        data["formations"].append({
            "diplome": form.get(f"diplome_{i}"),
            "etablissement": form.get(f"etablissement_{i}"),
            "debut": form.get(f"form_debut_{i}"),
            "fin": form.get(f"form_fin_{i}"),
            "description": form.get(f"form_desc_{i}")
        })
        i += 1

    data["request"] = request
    return template.TemplateResponse("cv.html", data)


# CRUD 
@app.post("/person/")
def create_person(person: Person, session: SessionDep):
    session.add(person)
    session.commit()
    session.refresh(person)
    return person

#@app.get("/")
