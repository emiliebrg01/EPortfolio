from sqlmodel import create_engine, Session

# 1. Nom de la base
sqlite_file_name = "database.db"

# 2. URL de connexion
sqlite_url = f"sqlite:///{sqlite_file_name}"

# 3. Création de l'engine -> connexion a la base de donnée
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False}  # obligatoire avec SQLite + FastAPI
)

# 4. Récupére la session
def get_session():
    with Session(engine) as session:
        yield session

