"""Description.

    Résoud le problème en donnant une sortie brute avec le gain total et une 
    
   liste comportant les tâches"""

from .donnees import Gains
import networkx as nx


def optimisation(gains: Gains) -> tuple:
    """Résoud le problème à l'aide de la bibliothèque networkx.

    A partir d'un objet de type Gains:
    - Crée un un graphe dirigé de n+2 niveaux avec n  la taille des vecteurs de l'objet;
    - Ajoute au début un noeud 'Initial' et à la fin un noeud 'Final';
    - Aux n niveaux il, y a trois noeuds 'Difficile', 'Facile', 'Repos';
    - La direction du graphe est du haut vers le bas ;
    - Un noeud 'Difficile' ne peut avoir comme précédent un noeud 'Facile' ou 'Diffile';
    - Les poids des liaisons correspondent au gains de la tâche succcédante et 0 au cas où cette dernière est 'Repos'/'Final';
    - Au premier niveau après 'Initial' le gain de la tâche 'Difficile' est de 0, pour empêcher le programme de choisir une tâche difficile dans la premère semaine. (La semaine 1 ne peut correspondre à une tâche difficle car cette dernière nécessite une semaine de repos en amont);
    - le programme cherche ensuite le chemin avec le poids total le plus élevé avec une fonction de nextworkx ainsi que le poids total du chemin;
    - Ensuite à partir de ce chemin on récupère le chemin avec les vrais termes du problème avec la liste 'ordre_execution',
    - On a en sortie le poids total et l'ordre d'exécution.
    >>> exemple = Gains([1000,500,1200,800,1500],[2000,1500,2500,1800,3000])

    >>> optimisation(exemple)
        (6500, ['Facile', 'Repos', 'Difficile', 'Repos', 'Difficile'])

    """
    n = len(gains.faciles)
    G = nx.DiGraph()
    for i in range(n):
        level = i + 1
        G.add_node((level, "F"), label="Facile")
        G.add_node((level, "D"), label="Difficile")
        G.add_node((level, "R"), label="Repos")
        if level == 1:
            # Créer le niveau 'initial' et ajouter des arêtes vers le niveau 1
            G.add_node(("Initial", "I"))
            G.add_edge(("Initial", "I"), (level, "F"), weight=gains.faciles[i])
            G.add_edge(("Initial", "I"), (level, "D"), weight=0)
            G.add_edge(("Initial", "I"), (level, "R"), weight=0)
        else:
            # Ajouter des arêtes entre les noeuds du niveau actuel et ceux du niveau précédent
            prev_level = level - 1
            G.add_edge((prev_level, "F"), (level, "F"), weight=gains.faciles[i])
            G.add_edge((prev_level, "F"), (level, "R"), weight=0)
            G.add_edge((prev_level, "D"), (level, "F"), weight=gains.faciles[i])
            G.add_edge((prev_level, "D"), (level, "R"), weight=0)
            G.add_edge((prev_level, "R"), (level, "F"), weight=gains.faciles[i])
            G.add_edge((prev_level, "R"), (level, "D"), weight=gains.difficiles[i])
            G.add_edge((prev_level, "R"), (level, "R"), weight=0)
    # Dernier noeud
    G.add_node(("Final", "F"))
    G.add_edge((n, "F"), ("Final", "F"), weight=0)
    G.add_edge((n, "D"), ("Final", "F"), weight=0)
    G.add_edge((n, "R"), ("Final", "F"), weight=0)

    # Calcul du gain
    gain = nx.dag_longest_path_length(G, weight="weight")

    # Récupéraction de l'ordre d'exécution:
    labels = [node[1] for node in nx.dag_longest_path(G, weight="weight")]
    ordre_execution = []
    for nom in labels:
        if nom == "F":
            ordre_execution.append("Facile")
        elif nom == "D":
            ordre_execution.append("Difficile")
        elif nom == "R":
            ordre_execution.append("Repos")

    return (gain, ordre_execution)
