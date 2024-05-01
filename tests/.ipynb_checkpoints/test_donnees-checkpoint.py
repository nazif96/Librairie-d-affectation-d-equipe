"""Description.

Tests automatiques de donnees.
"""
from applications.donnees import Gains
import pytest


def test_instanciation():
    essai = Gains([1000, 500, 1200, 800, 1500], [2000, 1500, 2500, 1800, 3000])
    isinstance(essai, Gains)


def test_egalité_nbr_semaines():
    with pytest.raises(
        ValueError, match="Il doit y avoir exactement le même nombre de semaines."
    ):
        Gains([10, 20], [5, 15, 25])


def test_semaines_min():
    with pytest.raises(
        ValueError,
        match="Il doit y avoir au moins deux semaines d'activités pour procéder à un arbitrage!",
    ):
        Gains([10], [5])


def test_facile_gains_positifs():
    with pytest.raises(
        ValueError, match="Les gains de tâches faciles ne peuvent être négatifs!"
    ):
        Gains([-10, 20, 30], [5, 15, 25])


def test_difficile_gains_positifs():
    with pytest.raises(
        ValueError, match="Les gains de tâches difficiles ne peuvent être négatifs!"
    ):
        Gains([10, 20, 30], [-5, 15, 25])


def test_affichage():
    gains = Gains([1000,500],[2000,1500])
    sortie = ' Semaine |Gain facile|Gain difficile|\n    1    |       1000|          2000| \n    2    |        500|          1500| \n'
    assert str(gains) == sortie





def test_gains_to_dict():
    gains = Gains([1000, 500, 1200, 800, 1500], [2000, 1500, 2500, 1800, 3000])
    expected_dict = {
        "faciles": [1000, 500, 1200, 800, 1500],
        "difficiles": [2000, 1500, 2500, 1800, 3000],
    }
    assert gains.to_dict() == expected_dict
