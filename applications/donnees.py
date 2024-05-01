"""Description.

Classe Permettant de représenter les données du problème d'optimisation.
"""

from dataclasses import dataclass


@dataclass
class Gains:
    """Représente les données d'un problème de type planification.

        faciles: liste des gains faciles
        difficiles: liste des gains difficiles


        Après instanciation, on vérifie si les données du problème sont raisonnables:
        - Les vecteurs de gains sont de même tailles et contiennent uniquement des valeurs positives,
        - Les vecteurs sont au moins de taille 2. Condition nécéssaire pour procéder à un arbitrage. Vu que la semaine 1 ne peut correspondre à une tâche difficile


        Les méthodes:
        - to_dict: permet de sérialiser préparer les données afin de les sérialiser avec json5
        - Str: permet de présenter le problème sous forme de tableau.


        >>> exemple = Gains([1000,500,1200,800,1500],[2000,1500,2500,1800,3000])


        >>> exemple
            Gains(faciles=[1000, 500, 1200, 800, 1500], difficiles=[2000, 1500, 2500, 1800, 3000])

        >>> print(exemple)
             Semaine |Gain facile|Gain difficile|
                1    |       1000|          2000|
                2    |        500|          1500|
                3    |       1200|          2500|
                4    |        800|          1800|
                5    |       1500|          3000|

        >>> exemple.to_dict()
            {'faciles': [1000, 500, 1200, 800, 1500],
    'difficiles': [2000, 1500, 2500, 1800, 3000]}
    """

    faciles: list
    difficiles: list

    def __post_init__(self):
        if len(self.faciles) != len(self.difficiles):
            raise ValueError("Il doit y avoir exactement le même nombre de semaines.")
        if len(self.faciles) < 2:
            raise ValueError(
                "Il doit y avoir au moins deux semaines d'activités pour procéder à un arbitrage!"
            )
        if any(facile < 0 for facile in self.faciles):
            raise ValueError("Les gains de tâches faciles ne peuvent être négatifs!")
        if any(difficile < 0 for difficile in self.difficiles):
            raise ValueError("Les gains de tâches difficiles ne peuvent être négatifs!")

    def to_dict(self):
        return {"faciles": self.faciles, "difficiles": self.difficiles}

    def __str__(cls):
        longueur_max_facile = max(
            [len(str(x)) for x in cls.faciles] + [len("Gain facile")]
        )
        longueur_max_difficile = max(
            [len(str(x)) for x in cls.difficiles] + [len("Gain difficile")]
        )

        # Première ligne du tableau
        objet = f" Semaine |{' ' * (longueur_max_facile - len('Gain facile'))}Gain facile|{' ' *(longueur_max_difficile - len('Gain difficile'))}Gain difficile|\n"

        # Boucle pour ajouter les données de chaque semaine du tableau
        for i in range(len(cls.faciles)):
            ligne = f"    {i+1}    |{' ' * (longueur_max_facile - len(str(cls.faciles[i])))}{cls.faciles[i]}|{' ' * (longueur_max_difficile - len(str(cls.difficiles[i])))}{cls.difficiles[i]}| \n"
            objet += ligne

        return objet
