# EPortfolio

Projet réalisé par **Maxence Baissas** et **Emilie Bourg** dans le cadre du cours Web Programming — EPF 4A.

## Objectif

Créer un site web permettant de générer un portfolio professionnel en remplissant un formulaire avec ses informations personnelles, expériences et formations.

## Stack technique

- **Backend :** FastAPI (Python)
- **Base de données :** SQLite via SQLModel
- **Templates :** Jinja2
- **Serveur :** Uvicorn (ASGI)

---

## Installation

### Prérequis

- Python 3.10 ou supérieur
- pip

### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd EPortfolio
```

### 2. Créer un environnement virtuel

**Windows (PowerShell)**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

```bash
pip install fastapi uvicorn sqlmodel jinja2 python-multipart
```

Si tu utilises l'authentification :
```bash
pip install passlib[bcrypt] itsdangerous
```

---

## Lancer l'application

### Option 1 — Python directement

**Windows**
```powershell
python main.py
```

**macOS / Linux**
```bash
python3 main.py
```

### Option 2 — Uvicorn avec rechargement automatique (recommandé en développement)

```bash
uvicorn main:app --reload
```

Puis ouvre ton navigateur sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Structure du projet

```
EPortfolio/
├── main.py               # Point d'entrée FastAPI, routes HTTP
├── database.py           # Configuration SQLite
├── auth.py               # Hachage et vérification des mots de passe
├── models/
│   └── model.py          # Modèles ORM (Person, Experience, Formation...)
├── repositories/
│   └── repository.py     # Accès base de données
├── services/
│   └── service.py        # Logique métier
├── schemas/
│   └── dto.py            # Objets de transfert de données
├── templates/
│   ├── form.html         # Formulaire de saisie du portfolio
│   ├── Template.html     # Affichage du portfolio généré
│   ├── login.html        # Page de connexion
│   └── register.html     # Page d'inscription
├── static/               # Fichiers CSS / JS statiques
└── database.db           # Base de données SQLite (générée automatiquement)
```

## Routes disponibles

| Méthode | Route       | Description                        |
|---------|-------------|----------------------------------  |
| GET     | `/`         | Formulaire de création du portfolio |
| POST    | `/generate` | Génère et affiche le portfolio      |
| GET     | `/login`    | Page de connexion                   |
| POST    | `/login`    | Traitement de la connexion          |
| GET     | `/register` | Page d'inscription                  |
| POST    | `/register` | Traitement de l'inscription         |
| GET     | `/logout`   | Déconnexion                         |
