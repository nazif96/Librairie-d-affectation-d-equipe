# But de la librairie
La présente libairie à pour but de résoudre les probèmes de type:

Une société de consultant doit organiser les affectations à venir d'une de ses équipes

Les travaux hebdomadaires disponibles sont soit faciles, soit difficiles.

Si on effectue un travail facile en semaine $i$, on obtient $l_i$ euros.
On obtient par contre $h_i$ pour un travail difficile.

Effectuer un travail difficile en semaine $i$ nécessite d'avoir eu une semaine
de repos en $i-1$.

Donner une organisation optimal étant donnés $l_1,\ldots,l_n$ et $h_1,\ldots,h_n$.

# Fonctionnalités
Nous avons développé cette bibliothèque dans une optique de gestion de plusieurs fichiers clients et ce de façon indépendantes. Ainsi on a les fonctionnalités suivantes:

## 1- Ajout d'un nouveau problème/fichier dune nouvelle entreprise $newcase$ :

Dans le terminal, entrez : **python -m poetry run python -m applications newcase nom_entreprise**      
> Veuillez entrer la durée des travaux (en semaines, minimum deux semaines):  1  
> Veuillez entrer la durée des travaux (en semaines, minimum deux semaines):  3  

$Sortie$:   
>Le fichier modèle (avec les gains à zéro) de nom_entreprise a été généré. Vous pouvez le modifier avec les données du réelles

Un fichier *nom_entreprise.json est crée* et contient les valeurs 0 pour toutes les tâches, il faudra le modifier manuellement avec les données du problème.


## 2- Voir les données d'un problème existant $view$ :

Dans le terminal, entrez : **python -m poetry run python -m applications view nom_entreprise**

$Sortie$: 
>
Semaine | Gain facile | Gain difficile |
------- | ----------- | -------------- |
1       | 0           | 0              |
2       | 0           | 0              |
3       | 0           | 0              |
  


## 3- Ajouter des tâches (semaines) à un problème $addweeks$:

Dans le terminal, entrez : **python -m poetry run python -m applications addweeks nom_entreprise**  

>Veuillez entrer le nombre de semaines à ajouter:  0  
Veuillez entrer le nombre de semaines à ajouter:  1  
 
$Sortie$: 
>Les nouvelles tâches ont été ajoutées à nom_entreprise avec les valeurs par 
défauts (0) à modifier!

Le fichier *nom_entreprise.json est mis à jour* avec les nouvelles semaines et leurs gains à zéro à modifier manuellement.


## 4- Résoudre un problème $plan$:  
Dans le terminal, entrez : **python -m poetry run python -m applications modify nom_entreprise**  

Pour les valeurs suivantes de gains :
- Faciles : [1, 1, 6, 50]
- Difficiles : [1, 3, 1000, 60]

On a :
 
> Le gain total est de 1051 euros.     
L'ordre d'exécution des tâches est le suivant :    
Semaine 1 : Facile      
Semaine 2 : Repos    
Semaine 3 : Difficile    
Semaine 4 : Facile     

## 6- Supprimer un fichier d'entreprise $suppr$:
Dans le terminal, entrez : **python -m poetry run python -m applications suppr nom_entreprise**

> Le problème nom_entreprise.json est supprimé avec succès.  

Le fichier *nom_entreprise.json est effacé* de notre repertoire.

**Remarque**: Si un problème n'est pas repertorié, on a le message suivant:  
> Nous n'avons pas cette entreprise dans notre répertoire! Vérifiez votre saisie ou créez un nouveau dossier avec la fonction dédiée.

## 7 - Menu d'aide  $help$:  
Dans le terminal, entrez : **python -m applications --help**

$Sortie$:  
Usage: python -m applications [OPTIONS] COMMAND [ARGS]...

Options:
- --install-completion : installe la complétion pour le shell actuel.
- --show-completion : montre la complétion pour le shell actuel afin de la copier ou personnaliser son installation.
- --help : Affiche ce message et quitte.

Commandes:
- addweeks : ajouter des travaux à un problème existant
- newcase : déclarer une nouvelle entreprise / nouveau problème
- plan : résoudre un problème déjà déclaré
- suppr : supprimer le fichier d'une entreprise
- view : affiche un problème déjà existant

## Auteurs:
- Nazifou AFOLABI
- Charbel AHOUANDOKOUN






