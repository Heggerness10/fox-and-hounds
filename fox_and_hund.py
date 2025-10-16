class GameBoard:
    """Classe représentant le plateau de jeu"""

    def __init__(self, size):
        """
        Constructeur du plateau de jeu
        :param size: nombre de lignes et colonnes (doit être multiple de 4)
        """
        # S'assurer que size est un multiple de 4
        # Si size = 5, on prend 8 (le prochain multiple de 4)
        if size % 4 != 0:
            size = ((size // 4) + 1) * 4

        self.__size = size
        
        # Créer le plateau : une liste de listes remplies de 0
        self.__board = []
        for i in range(size):
            ligne = [0] * size  # Une ligne de 0
            self.__board.append(ligne)

        # === INITIALISATION DES HOUNDS ===
        # Les hounds sont sur la ligne 0, colonnes impaires (1, 3, 5, ...)
        hound_num = 1
        for col in range(1, size, 2):  # 1, 3, 5, 7...
            self.__board[0][col] = hound_num
            hound_num += 1

        # === INITIALISATION DU FOX ===
        # Le fox est sur la dernière ligne, colonne du milieu
        fox_col = size // 2
        fox_row = size - 1
        self.__board[fox_row][fox_col] = -1

    def display(self):
        """Affiche le plateau de jeu"""
        for row in self.__board:
            line = ""
            for cell in row:
                if cell == 0:
                    line += ". "  # Case vide
                elif cell == -1:
                    line += "F "  # Fox (corrigé : était "W")
                else:
                    line += str(cell) + " "  # Numéro du hound
            print(line)
        print()  # Ligne vide après le plateau

    def get_cell(self, row, col):
        """
        Getter pour obtenir la valeur d'une case
        :param row: numéro de ligne
        :param col: numéro de colonne
        :return: valeur de la case, ou None si hors limites
        """
        # Vérifier que les coordonnées sont valides
        if 0 <= row < self.__size and 0 <= col < self.__size:
            return self.__board[row][col]
        return None

    def set_cell(self, row, col, value):
        """
        Setter pour modifier la valeur d'une case
        :param row: numéro de ligne
        :param col: numéro de colonne
        :param value: nouvelle valeur
        """
        # Vérifier que les coordonnées sont valides
        if 0 <= row < self.__size and 0 <= col < self.__size:
            self.__board[row][col] = value

    def get_size(self):
        """Retourne la taille du plateau"""
        return self.__size


class Hound:
    """Classe représentant un pion hound"""

    def __init__(self, row=0, col=0):
        """
        Constructeur avec valeurs par défaut
        :param row: numéro de ligne (par défaut 0)
        :param col: numéro de colonne (par défaut 0)
        """
        self.__row = row
        self.__col = col

    def get_row(self):
        """Retourne la ligne du pion"""
        return self.__row

    def get_col(self):
        """Retourne la colonne du pion"""
        return self.__col

    def set_position(self, row, col):
        """Modifie la position du pion"""
        self.__row = row
        self.__col = col

    def can_move_to(self, board, row, col):
        """
        Vérifie si le hound peut se déplacer vers la case (row, col)
        Les hounds se déplacent en diagonale vers le bas uniquement
        
        :param board: plateau de jeu
        :param row: ligne de destination
        :param col: colonne de destination
        :return: True si le mouvement est possible, False sinon
        """
        # ÉTAPE 1 : Vérifier que la destination est dans les limites du plateau
        if row < 0 or row >= board.get_size():
            return False
        if col < 0 or col >= board.get_size():
            return False

        # ÉTAPE 2 : Calculer le déplacement
        row_diff = row - self.__row  # Différence de lignes
        col_diff = abs(col - self.__col)  # Différence de colonnes (valeur absolue)

        # ÉTAPE 3 : Vérifier que c'est un mouvement diagonal vers le bas
        # Le hound doit descendre d'exactement 1 ligne (row_diff = 1)
        # et se déplacer de 1 colonne à gauche ou à droite (col_diff = 1)
        if row_diff != 1 or col_diff != 1:
            return False

        # ÉTAPE 4 : Vérifier que la case de destination est vide
        if board.get_cell(row, col) != 0:
            return False

        return True

    def can_move(self, board):
        """
        Vérifie s'il existe au moins une case où le hound peut se déplacer
        
        :param board: plateau de jeu
        :return: True s'il peut bouger, False sinon
        """
        # Un hound peut aller en bas-gauche ou en bas-droite
        # Tester les 2 possibilités
        
        # Possibilité 1 : bas-gauche
        if self.can_move_to(board, self.__row + 1, self.__col - 1):
            return True
        
        # Possibilité 2 : bas-droite
        if self.can_move_to(board, self.__row + 1, self.__col + 1):
            return True

        # Aucune des 2 directions n'est possible
        return False

    def move(self, board):
        """
        Demande à l'utilisateur de saisir les coordonnées et déplace le hound
        
        :param board: plateau de jeu
        """
        while True:
            try:
                # Demander les coordonnées
                row = int(input("Which row ? "))
                col = int(input("Which column ? "))

                # Ajuster pour l'indexation (l'utilisateur compte à partir de 1)
                row -= 1
                col -= 1

                # Vérifier si le mouvement est valide
                if self.can_move_to(board, row, col):
                    # Récupérer le numéro du hound
                    old_value = board.get_cell(self.__row, self.__col)
                    
                    # Effacer l'ancienne position
                    board.set_cell(self.__row, self.__col, 0)

                    # Placer le hound à la nouvelle position
                    board.set_cell(row, col, old_value)
                    
                    # Mettre à jour les attributs
                    self.__row = row
                    self.__col = col
                    
                    break  # Sortir de la boucle, le mouvement est fait
                    
            except ValueError:
                # Si l'utilisateur entre quelque chose qui n'est pas un nombre
                pass  # On recommence la boucle


class Fox(Hound):
    """Classe représentant le pion fox (hérite de Hound)"""

    def __init__(self, row=0, col=0):
        """Constructeur du fox"""
        # Appeler le constructeur de la classe parent (Hound)
        super().__init__(row, col)

    def can_move_to(self, board, row, col):
        """
        Vérifie si le fox peut se déplacer vers la case (row, col)
        Le fox se déplace en diagonale dans TOUTES les directions
        (différence avec hound qui va seulement vers le bas)
        
        :param board: plateau de jeu
        :param row: ligne de destination
        :param col: colonne de destination
        :return: True si le mouvement est possible, False sinon
        """
        # ÉTAPE 1 : Vérifier que la destination est dans les limites
        if row < 0 or row >= board.get_size():
            return False
        if col < 0 or col >= board.get_size():
            return False

        # ÉTAPE 2 : Calculer le déplacement
        row_diff = abs(row - self.get_row())  # Valeur absolue (haut ou bas)
        col_diff = abs(col - self.get_col())  # Valeur absolue (gauche ou droite)

        # ÉTAPE 3 : Vérifier que c'est un mouvement diagonal
        # Le fox peut aller dans les 4 directions diagonales
        if row_diff != 1 or col_diff != 1:
            return False

        # ÉTAPE 4 : Vérifier que la case de destination est vide
        if board.get_cell(row, col) != 0:
            return False

        return True

    def win(self):
        """
        Vérifie si le fox a gagné (atteint la première ligne)
        
        :return: True si le fox a gagné, False sinon
        """
        return self.get_row() == 0


class FoxAndHounds:
    """Classe principale pour gérer une partie"""

    def __init__(self, size=8):
        """
        Constructeur du jeu
        :param size: taille du plateau (par défaut 8x8)
        """
        # Créer le plateau de jeu
        self.__board = GameBoard(size)

        # Récupérer la taille réelle (ajustée si nécessaire)
        actual_size = self.__board.get_size()

        # === INITIALISATION DU FOX ===
        # Le fox commence sur la dernière ligne, au milieu
        fox_row = actual_size - 1
        fox_col = actual_size // 2
        self.__fox = Fox(fox_row, fox_col)

        # === INITIALISATION DES HOUNDS ===
        # Il y a actual_size/2 hounds (2 pour 4x4, 4 pour 8x8, etc.)
        self.__hounds = []
        nb_hounds = actual_size // 2
        
        for i in range(nb_hounds):
            col = 1 + i * 2  # Colonnes 1, 3, 5, 7...
            self.__hounds.append(Hound(0, col))

    def play(self):
        """Méthode pour jouer une partie complète"""
        game_over = False

        while not game_over:
            # ========== AFFICHER LE PLATEAU ==========
            self.__board.display()

            # ========== TOUR DU FOX ==========
            print("Fox to move :")
            self.__fox.move(self.__board)

            # Vérifier si le fox a gagné (atteint la ligne 0)
            if self.__fox.win():
                self.__board.display()
                print("Fox wins")
                game_over = True
                break

            # Afficher le plateau après le mouvement du fox
            self.__board.display()

            # ========== TOUR DES HOUNDS ==========
            # Étape 1 : Trouver quels hounds peuvent bouger
            movable_hounds = []
            for i in range(len(self.__hounds)):
                if self.__hounds[i].can_move(self.__board):
                    movable_hounds.append(i)

            # Étape 2 : Si aucun hound ne peut bouger
            if len(movable_hounds) == 0:
                # Vérifier si le fox peut encore bouger
                if not self.__fox.can_move(self.__board):
                    print("Draw - nobody can move")
                    game_over = True
                    break
                else:
                    # Seul le fox peut bouger, on continue avec son tour
                    continue

            # Étape 3 : Demander au joueur de choisir un hound
            hound_index = -1
            while hound_index not in movable_hounds:
                try:
                    choice = int(input("Choose a hound : "))
                    hound_index = choice - 1  # Ajuster pour l'index (0-based)
                except ValueError:
                    pass  # Redemander si ce n'est pas un nombre

            # Étape 4 : Déplacer le hound choisi
            print(f"Hound n°{hound_index + 1} to move :")
            self.__hounds[hound_index].move(self.__board)

            # Étape 5 : Vérifier si le fox peut encore bouger
            if not self.__fox.can_move(self.__board):
                self.__board.display()
                print("Hounds win")
                game_over = True


# ========== LANCER UNE PARTIE ==========
if __name__ == "__main__":
    game = FoxAndHounds(8)  # Créer une partie sur un plateau 8x8
    game.play()  # Lancer la partie