"""Description.

Application ligne de commande pour la librairie.
"""

from .donnees import Gains
from .planification import planing
import json5
import typer
import os
from rich import print

gains_faciles = []
gains_difficiles = []
Message = """Nous n'avons pas cette entreprise dans notre répertoire! 
Vérifiez votre saisie ou créez un nouveau fichier avec la fonction dédiée."""
application = typer.Typer()


@application.command(help="déclarer une nouvelle entreprise/nouveau problème")
def newcase(nom_entreprise: str):
    nb_semaines = 0
    while nb_semaines < 2:
        nb_semaines = int(
            input(
                "Veuillez entrer la durée des travaux (en semaines, minimum deux semaines):  "
            )
        )
    for i in range(nb_semaines):
        gains_faciles.append(0)
        gains_difficiles.append(0)

    taches = Gains(gains_faciles, gains_difficiles)

    with open(nom_entreprise + ".json", "w") as fichier:
        json5.dump(taches.to_dict(), fichier)
    fichier.close()
    print (f"Le fichier modèle (avec les gains à zéro) de {nom_entreprise} a été généré. Vous pouvez le modifier avec les données du réelles")
    os.startfile(nom_entreprise + ".json")


@application.command(help="résoudre un problème déjà déclaré")
def plan(nom_entreprise: str):
    if os.path.exists(nom_entreprise + ".json"):
        with open(nom_entreprise + ".json", "r") as fichier:
            data = json5.load(fichier)
        fichier.close()
        gains = Gains(**data)
        solution = planing(gains)
        print(solution)
    else: 
        print(Message)


@application.command(help="supprimer le fichier d'une entreprise")
def suppr(nom_entreprise: str):
    if os.path.exists(nom_entreprise + ".json"):
        os.remove(nom_entreprise + ".json")
        print(f" Le problème {nom_entreprise}" + ".json est supprimé avec succès.")
    else:
        print(Message)


@application.command(help="ajouter des travaux à un problème existant")
def addweeks(nom_entreprise: str):
    if os.path.exists(nom_entreprise + ".json"):
        nb_semaines = 0
        while nb_semaines < 1:
            nb_semaines = int(
                input("Veuillez entrer le nombre de semaines à ajouter:  ")
            )
        with open(nom_entreprise + ".json", "r") as fichier:
            data = json5.load(fichier)
        fichier.close()
        gains = Gains(**data)
        os.remove(nom_entreprise + ".json")
        for i in range(nb_semaines):
            gains.faciles.append(0)
            gains.difficiles.append(0)
        with open(nom_entreprise + ".json", "w") as fichier:
            json5.dump(gains.to_dict(), fichier)
        fichier.close()
        print(f"Les nouvelles tâches ont été ajoutées à {nom_entreprise} avec les valeurs par défauts (0) à modifier!")
    else:
        print(Message)



@application.command(help="affiche un problème déjà existant")
def view(nom_entreprise: str):
    if os.path.exists(nom_entreprise + ".json"):
        with open(nom_entreprise + ".json", "r") as fichier:
            data = json5.load(fichier)
        fichier.close()
        gains = Gains(**data)
        print(str(gains))
    else:
        print(Message)


if __name__ == "__main__":
    application()
