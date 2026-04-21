# ## Fichier main ##

#################
#### IMPORTS ####
#################
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel
from database import engine

from models.person_model import Person

# Initialisation FastAPI 

app = FastAPI()
template = Jinja2Templates(directory="templates")

# Creation des bases de données au demarrage
SQLModel.metadata.create_all(engine)



# Routers

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    context = {
        "request": request,
        "name": "Baissas",
        "firstname": "Maxence",
        "phone": "0615154270",
        "mail": "maxence.baissas@epfedu.fr",
        "experiences": [],
        "formations": [],
    }
    return template.TemplateResponse(request, "template.html", context=context)


