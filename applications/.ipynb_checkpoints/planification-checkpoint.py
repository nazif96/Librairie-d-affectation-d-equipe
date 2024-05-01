"""Description.

    Résoud le problème en donnant une sortie plus stylisée et adaptée à une présentation"""

from .optimisation import optimisation
from .donnees import Gains
from rich import print


def planing(vect_gains: Gains) -> str:
    """ Présente le résultat d'optimisation sous une forme plus appréhensible.
    
    Le programme applique la fonction optimisation à l'objet Gains. 
    Puis à l'aide concaténation et f-strings donne le gain total ainsi que la tâche par semaine.
    
    >>> exemple = Gains([1000,500,1200,800,1500],[2000,1500,2500,1800,3000])
    
    >>> optimisation(exemple)
        Le gain total est de 6500 euros.
        L'ordre d'exécution des tâches est le suivant :
        Semaine 1 : Facile 
        Semaine 2 : Repos 
        Semaine 3 : Difficile 
        Semaine 4 : Repos 
        Semaine 5 : Difficile 
    """
    optimisation(vect_gains)
    print("Le gain total est de", optimisation(vect_gains)[0], "euros.")
    print("L'ordre d'exécution des tâches est le suivant :")
    for i in range(len(vect_gains.faciles)):
        print(f"Semaine {i+1} : {optimisation(vect_gains)[1][i]} ")
