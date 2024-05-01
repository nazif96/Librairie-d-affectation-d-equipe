"""Description.

Tests automatiques de la fonction optimisation.
"""

from applications.donnees import Gains
from applications.optimisation import optimisation


def test_optimisation_1():
    entree = Gains([1000, 500, 1200, 800, 1500], [2000, 1500, 2500, 1800, 3000])
    sortie = (6500, ["Facile", "Repos", "Difficile", "Repos", "Difficile"])
    assert optimisation(entree) == sortie


def test_optimisation_2():
    entree = Gains([4500, 6000, 5555], [5673, 7600, 5638])
    sortie = (16055, ["Facile", "Facile", "Facile"])
    assert optimisation(entree) == sortie


def test_optimisation_3():
    entree = Gains([20, 0, 100, 20], [20, 200, 20, 400])
    sortie = (600, ["Repos", "Difficile", "Repos", "Difficile"])
    assert optimisation(entree) == sortie


def test_optimisation_4():
    entree = Gains([5, 8, 20], [10, 20, 30])
    sortie = (40, ["Repos", "Difficile", "Facile"])
    assert optimisation(entree) == sortie
    
    
def test_optimisation_5():
    entree = Gains([1,3,500],[1,6,1000])
    sortie = (1001, ["Facile", "Repos", "Difficile"])
    assert optimisation(entree) == sortie
    

