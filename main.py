## Fichier main ##

# Les classes à creer ! (chaque classe sera une partie du portfolio)

# Classe personne (about me) : firstname, lastname, age, statut
# Classe contact (mail, tel, linkdln, adress)
#
#
# Classe expériences (name, year, place, skills, only (bool), status, )
# Classe contact
# Classe temoignage


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
    def __ini__(self, email, phone, linkdln, adress):
        self.user_email = email
        self.user_phone = phone
        self.user_linkdln = linkdln
        self.user_adress = adress


class Projects:
    def __init__(self, name, year, place, skills, only, status):
        self.project_name = name
        self.project_year = year
        self.project_place = place
        self.project_skills = skills
        self.project_only = only
        self.project_status = status


class testimonials:
    def __init__():
        return None


# Surement que methode CRON elle sera gerer ailleurs
