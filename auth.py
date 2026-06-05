import bcrypt


def hash_password(password: str) -> str:
    # Hache le mot de passe avec un sel aléatoire via bcrypt.
    # Le sel garantit que deux mots de passe identiques produisent des hashs différents.
    # Utilisé à l'inscription avant de stocker le mot de passe en base.
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compare un mot de passe en clair avec son hash stocké en base.
    # bcrypt re-hache le mot de passe avec le sel extrait du hash, puis compare.
    # Utilisé à la connexion. Retourne True si le mot de passe est correct.
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )
