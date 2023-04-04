# Jeu de Sudoku

**Description du Projet**

Une implémentation d’un jeu Sudoku en langage Python selon l’approche orientée objet.

 *Le sudoku est un jeu de logique consistant à remplir une grille carrée de 9 x 9 cases, avec des chiffres allant de 1 à 9, les règles sont simples : Un chiffre
 ne pourra être présent qu'une seule fois sur chaque ligne, colonne, et région (subdivision carrée de 3 x 3 cases).*
 
 **L’interface qui s’affiche à l’exécution du programme**
 
 
 ![sudoku 1](https://user-images.githubusercontent.com/100292443/167278079-a3d6a434-43e5-4ce6-906d-cd70f61b284c.png) 
 
 L’utilisateur peut choisir le niveau de complexité et cliquer sur le bouton « nouvelle partie » pour afficher l’interface du jeu et commencer à jouer.


Dans ce programme, 4 classes sont définies :

**La classe Tuile :** un objet de la classe Tuile représente une cellule d’une matrice sudoku et contient l'information par rapport à la valeur de tuile,
sa position sur la ligne (de la matrice) et sa position sur la colonne (de la matrice).

**La classe Sudoku :** un objet de la classe représente une matrice contenant 81 cellules, chaque cellule comporte un objet de la classe Tuile.

   La valeur initiale de tout les tuile est égale a zéro. 
   
 Le constructeur de la classe Sudoku prend comme paramètre l’état de jeu, c’est à dire le niveau de complexité choisi par l’utilisateur.
 
 Cette classe a 3 méthodes principales :
 
**La méthode « possible (self,ln,cl,num)» :** qui permet de vérifier si on peut assigner à la ligne « ln » et la colonne « cl » la valeur num .

**La méthode « solution(self,ln,cl) » :** qui permet de remplir une matrice valide en suivant les règles de jeu .

**La méthode « generer_matrice(self) » :** permet de récupérer la matrice générée par la méthode solution et la modifier selon le niveau de complexité de jeu.

    Si le niveau choisi est Simple : assigner la valeur 0 à 25 cellules de la matrice choisies aléatoirement.
 
    Si le niveau choisi est Moyen : assigner la valeur 0 à 40 cellules de la matrice choisies aléatoirement.

    Si le niveau choisi est Avance : assigner la valeur 0 à 55 sellules de la matrice choisies aléatoirement.

Les 2 autres classes représentent les deux interfaces (interface utilisateur et interface de jeu).

**L’interface de jeu :**


![sudoku2](https://user-images.githubusercontent.com/100292443/167278469-0ef44d23-d7b2-4654-904f-999e3be3c7f5.png)



Comporte la grille de sudoku ou l’utilisateur peut entrer des chiffres et les boutons suivants :

**Supprimer :** Supprimer les valeurs entrées 

**Évaluer :** évaluer les valeurs entrées par l’utilisateur, si la valeur est correcte elle va s’afficher en vert, sinon en rouge.


![sudoku3](https://user-images.githubusercontent.com/100292443/167278482-e02f8c12-1c8f-494f-b855-ba881869b3ac.png)


**Terminer :** terminer le jeu, afficher la matrice résolue et afficher dans une zone de texte si l’utilisateur a réussi, afficher les erreurs et les corrections le cas
contraire.

![sudoku 3](https://user-images.githubusercontent.com/100292443/167278484-4d50e4d0-3fe5-4c54-b427-b667b8d35b37.png)


**Quitter :** fermer la fenêtre , sortir du programme.


**Installation :**

Ce projet ne nécessite aucune installation de logiciels ou bibliothèque supplémentaire.

**Auteur et reconnaissance:**

Ce projet a été réalisé par Nabila Amiour et Noureddine Bensghir , sous la supervision de l’enseignant : Keven presseau-St-Laurent.

**État du projet:**

Projet terminé





