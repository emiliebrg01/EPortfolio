# ## Fichier main ##

#################
#### IMPORTS ####
#################
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlmodel import SQLModel
from database import engine
from models import model

from starlette.middleware.sessions import SessionMiddleware
from fastapi import Depends
from sqlmodel import Session
from database import get_session
from services.service import register_user, login_user
from schemas.dto import UserRegisterDTO, UserLoginDTO

# Initialisation FastAPI
app = FastAPI()
template = Jinja2Templates(directory="templates")
app.mount("/styles", StaticFiles(directory="styles"), name="styles") # lie l'url "/styles" au dossier local styles

load_dotenv()

secret_key = os.getenv("SESSION_SECRET_KEY")
app.add_middleware(SessionMiddleware, secret_key=secret_key, max_age=1800)


# Creation des bases de données au demarrage
SQLModel.metadata.create_all(engine)


# Routers
@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return template.TemplateResponse(request, "login.html", {"request": request})


@app.post("/login")
async def post_login(request: Request, session: Session = Depends(get_session)):
    data = await request.form()
    user_data = UserLoginDTO(username=data["username"], password=data["password"])
    user = login_user(session, user_data)
    if not user:
        return template.TemplateResponse(
            request,
            "login.html",
            {"request": request, "error": "Identifiants invalides"},
        )
    request.session["user_id"] = user.id
    request.session["username"] = user.username
    return RedirectResponse(url="/", status_code=302)


@app.get("/register", response_class=HTMLResponse)
def get_register(request: Request):
    return template.TemplateResponse(request, "register.html", {"request": request})


@app.post("/register")
async def post_register(request: Request, session: Session = Depends(get_session)):
    data = await request.form()
    user_data = UserRegisterDTO(
        username=data["username"], email=data["email"], password=data["password"]
    )
    user, error = register_user(session, user_data)
    if not user:
        return template.TemplateResponse(
            request,
            "register.html",
            {"request": request, "error": error},
        )
    return RedirectResponse(url="/login", status_code=302)


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)


@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    if not request.session.get("user_id"):
        return RedirectResponse(url="/login", status_code=302)
    return template.TemplateResponse(request, "form.html", context={"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate_port(request: Request):
    if not request.session.get("user_id"):
        return RedirectResponse(url="/login", status_code=302)
    data_form = (
        await request.form()
    )  # recupere les données envoyées par le formulaire HTML

    # Récupere les champs simple du formulaire
    firstname = data_form.get("firstname", "")
    name = data_form.get("name", "")
    mail = data_form.get("mail", "")
    phone = data_form.get("phone", "")
    linkedin = data_form.get("linkedin", "")

    # Création de listes pour stocker les experiences, informations, skills
    experiences = []
    formations = []
    skills = []

    # Création de set pour reperer les indexes et éviter les doublons
    exp = set()
    form = set()
    sk = set()

    # Repere les indexs
    for key in data_form.keys():
        if key.startswith("job_"):
            exp.add(key.split("_")[1])
        if key.startswith("formation_"):
            form.add(key.split("_")[1])
        if key.startswith("name_"):
            sk.add(key.split("_")[2])
    
    # Reconstruit les experiences 
    for index in sorted(exp, key=int):
        experiences.append(
            {
                "job": data_form.get(f"job_{index}", ""),
                "company": data_form.get(f"company_{index}", ""),
                "start": data_form.get(f"exp_start_{index}", ""),
                "end": data_form.get(f"exp_end_{index}", ""),
                "description": data_form.get(f"exp_desc_{index}", ""),
            }
        )

    # Reconstruits les formations
    for index in sorted(form, key=int):
        formations.append(
            {
                "formation": data_form.get(f"formation_{index}", ""),
                "university": data_form.get(f"university_{index}", ""),
                "start": data_form.get(f"form_start_{index}", ""),
                "end": data_form.get(f"form_end_{index}", ""),
                "description": data_form.get(f"form_desc_{index}", ""),
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
    
    context = {
        "request" : request,
        "firstname" : firstname,
        "name" : name,
        "mail" : mail,
        "phone" : phone,
        "linkedin": linkedin,
        "experiences" : experiences,
        "formations" : formations,
        "skills": skills,
    }

    return template.TemplateResponse(request, "Template.html", context=context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
