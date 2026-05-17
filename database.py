from sqlmodel import create_engine, Session

# URL de connexion
sqlite_url = "sqlite:///database.db"

# Création de l'engine -> connexion a la base de donnée
engine = create_engine(sqlite_url) 

# Récupére la session
def get_session():
    with Session(engine) as session:
        yield session

