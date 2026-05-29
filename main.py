# ## Fichier main ##

#################
#### IMPORTS ####
#################
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlmodel import SQLModel
from database import engine
from models import model

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
        context={"request":request}
    )

@app.post("/generate", response_class=HTMLResponse)
async def generate_port(request:Request):

    data_form = await request.form() # recupere les données envoyées par le formulaire HTML

    # Récupere les champs simple du formulaire
    firstname = data_form.get("firstname", "")
    name = data_form.get("name", "")
    mail = data_form.get("mail", "")
    phone = data_form.get("phone", "")

    # Création de listes pour stocker les experiences et informations
    experiences = []
    formations = []

    # Création de set pour reperer les indexes et éviter les doublons 
    exp = set()
    form = set()

    # Repere les indexs
    for key in data_form.keys():
        if key.startswith("job_"):
            exp.add(key.split("_")[1])
        if key.startswith("formation_"):
            form.add(key.split("_")[1])
    
    # Reconstruit les experiences et formations
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

    context = {
        "request" : request,
        "firstname" : firstname,
        "name" : name,
        "mail" : mail,
        "phone" : phone,
        "experiences" : experiences,
        "formations" : formations,
    }

    return template.TemplateResponse(
        request,
        "Template.html",
        context=context
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
