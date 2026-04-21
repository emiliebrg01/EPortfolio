# ## Fichier main ##

#################
#### IMPORTS ####
#################
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import create_engine, Session
from typing import Annotated


# Initialisation FastAPI 

app = FastAPI()
template = Jinja2Templates(directory="templates")

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


