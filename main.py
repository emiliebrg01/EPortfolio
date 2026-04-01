## Fichier main ##

# Les classes à creer ! (chaque classe sera une partie du portfolio)

# Classe personne (about me) : firstname, lastname, age, statut
# Classe contact (mail, tel, linkdln, adress)
#
#
# Classe expériences (name, year, place, skills, only (bool), status, )
# Classe contact
# Classe temoignage


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

class Person:
    def __init__(self, firstname, lastname, age, status):
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_age = age
        self.statut = status

    def create_person():
        return None

    def get_person():
        return None

    def put_person():
        return None

    def delete_person():
        return None


class Contact:
    def __init__(self, email, phone, linkdln, adress):
        self.user_email = email
        self.user_phone = phone
        self.user_linkdln = linkdln
        self.user_adress = adress


class Project:
    def __init__(self, name, year, place, skills, only, status):
        self.name = name
        self.year = year
        self.place = place
        self.skills = skills
        self.only = only
        self.status = status


class testimonials:
    def __init__():
        return None


# Surement que methode CRUB elle sera gerer ailleurs

template = Jinja2Templates(directory="templates")

app = FastAPI()

name=["Maxence"]

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    context = {}
    return template.TemplateResponse(request, "Template.html", context=context)
