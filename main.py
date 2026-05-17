# ## Fichier main ##

#################
#### IMPORTS ####
#################
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlmodel import SQLModel
from database import engine
from models import model

# Initialisation FastAPI 
app = FastAPI()
template = Jinja2Templates(directory="templates")

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

    # Création de set pour éviter les doublons 
    exp = set()
    format = set()

    for key in data_form.keys():
        if key.startwith("poste"):
            exp.add(key.split("_")[1])
        if key.startwith()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
