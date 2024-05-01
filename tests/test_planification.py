"""Description.

Tests automatiques de la fonction planing.
"""


from applications.donnees import Gains
from applications.planification import planing
import io
import sys


def test_planing_1():
    entree = Gains([1000, 500, 1200, 800, 1500], [2000, 1500, 2500, 1800, 3000])
    with io.StringIO() as output:
        sys.stdout = output
        planing(entree)
        assert (
            output.getvalue()
            == """Le gain total est de 6500 euros.
L'ordre d'exécution des tâches est le suivant :
Semaine 1 : Facile 
Semaine 2 : Repos 
Semaine 3 : Difficile 
Semaine 4 : Repos 
Semaine 5 : Difficile 
"""
        )
    sys.stdout = sys.__stdout__


def test_planing_2():
    entree = Gains([4500, 6000, 5555], [5673, 7600, 5638])
    with io.StringIO() as output:
        sys.stdout = output
        planing(entree)
        assert (
            output.getvalue()
            == """Le gain total est de 16055 euros.
L'ordre d'exécution des tâches est le suivant :
Semaine 1 : Facile 
Semaine 2 : Facile 
Semaine 3 : Facile 
"""
        )
    sys.stdout = sys.__stdout__


def test_planing_3():
    entree = Gains([20, 0, 100, 20], [20, 200, 20, 400])
    with io.StringIO() as output:
        sys.stdout = output
        planing(entree)
        assert (
            output.getvalue()
            == """Le gain total est de 600 euros.
L'ordre d'exécution des tâches est le suivant :
Semaine 1 : Repos 
Semaine 2 : Difficile 
Semaine 3 : Repos 
Semaine 4 : Difficile 
"""
        )
    sys.stdout = sys.__stdout__


def test_planing_4():
    entree = Gains([5, 8, 20], [10, 20, 30])
    with io.StringIO() as output:
        sys.stdout = output
        planing(entree)
        assert (
            output.getvalue()
            == """Le gain total est de 40 euros.
L'ordre d'exécution des tâches est le suivant :
Semaine 1 : Repos 
Semaine 2 : Difficile 
Semaine 3 : Facile 
"""
        )
    sys.stdout = sys.__stdout__
