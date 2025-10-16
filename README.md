# Fox and Hounds

# Description du projet
Fox and Hounds est un jeu de stratégie développé en Python par les 3M : Matt, Mamadou et Mouhamadou.  
Le jeu se joue sur un plateau carré où un renard (Fox) tente d’échapper à plusieurs chiens (Hounds).  
Le but du renard est d’atteindre la première ligne du plateau sans se faire bloquer, tandis que les chiens doivent l’en empêcher.


# Règles du jeu
- Le plateau est de taille n × n (ajusté automatiquement au multiple de 4 le plus proche).  
- Le renard (F) commence sur la dernière ligne, au milieu.  
- Les chiens (1, 2, 3, …) sont placés sur la première ligne, sur les colonnes paires.  
- Le renard peut se déplacer en diagonale dans toutes les directions.  
- Les chiens ne peuvent se déplacer qu’en diagonale vers le bas.  
- Le jeu se termine :
  Si le renard atteint la première ligne → le renard gagne  
  Si le renard est bloqué → les chiens gagnent


# Lancement du jeu
1. Prérequis
- Avoir Python 3 installé sur votre machine.  
- Ouvrir le projet dans un terminal ou dans VS Code.

2. Exécution
Dans le terminal, exécutez :

python3 fox_and_hounds.py

Le jeu vous demandera :
- de choisir la taille du plateau (ex : 4, 8, 12…)  
- puis d’entrer les positions des pions à déplacer.


# Structure du projet

FoxAndHounds
│
├── fox_and_hounds.py           # Point d’entrée du jeu
└── README.md         # Documentation du projet


# Fonctionnement du code
- GameBoard → crée le plateau, affiche la grille et gère les cellules.  
- Hound → définit le comportement des chiens (mouvements vers le bas).  
- Fox → hérite de Hound, mais peut se déplacer dans toutes les directions.  
- FoxAndHounds → gère la logique complète du jeu, les tours et les conditions de victoire.


# Améliorations possibles
- Ajouter une interface graphique  
- Intégrer un mode IA pour affronter l’ordinateur.  
- Ajouter un système de sauvegarde de partie.  
- Créer un mode 2 joueurs en ligne.


# Auteurs
Projet réalisé par le groupe 3M :
- Mohamed Ahid Matt
- Mamadou Heggernes Sadio
- Mouhamadou Sy


