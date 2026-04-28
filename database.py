from sqlmodel import create_engine, Session

# URL de connexion
postgresql_url = "postgresql://postgres:777@localhost:5432/portfolio"

# Création de l'engine -> connexion a la base de donnée
engine = create_engine(postgresql_url) 

# Récupére la session
def get_session():
    with Session(engine) as session:
        yield session

