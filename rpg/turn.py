# État global
#
# tour_actuel (n° de manche)
# joueur_actif (index ou nom)
# phase (ex. "exploration", "combat", "dialogue")
# game_over (bool)
# Schéma minimal de boucle
#
# Tant que not game_over :
#
# Afficher un résumé rapide (PV, mana, position, quêtes).
# Présenter un menu d’actions au joueur actif.
# [1] Se déplacer
# [2] Interagir (PNJ, coffre…)
# [3] Combattre
# [4] Inventaire / équipement
# [5] Feuille de personnage
# [0] Quitter la partie
# Lancer la fonction associée à son choix (déplacement, attaque, dialogue, inventaire, etc.).
# Passer au joueur suivant, ou à la manche suivante si tu veux que les monstres/NPC réagissent entre chaque tour.
# Fin de partie : déclenchée si tous les joueurs sont morts ou si un objectif global est atteint (ex. boss final battu).
from curses.ascii import isalnum

from rpg.player import Player


class Turn:
    def __init__(self, players: dict[str, Player]):
        self.current_turn = 1
        self.current_player = None #Name
        self.players = players
        self.phase = "exploration"
        self.game_over = False

    def play(self):
        first_player = input("Qui est le premier joueur à commencé ? ")
        self.current_player = first_player
        while not self.game_over:
            self.show_state_of_game()
            self.action_menu()

    def get_current_player_name(self):
        return self.players[self.current_player]

    def show_state_of_game(self):
        print("=====GAME======")
        print(f"Tour actuel : {self.current_turn}")
        print(f"Joueur actuel: {self.current_player}")
        print(f"Phase de jeu : {self.phase}")
        print("===============")

    def action_menu(self):
        print("=====ACTION MENU======")
        print("[1] Se déplacer")
        print("[2] Interagir (PNJ, coffre…)")
        print("[3] Combattre")
        print("[4] Inventaire / équipement")
        print("[5] Feuille de personnage")
        print("[0] Quitter la partie")
        print("Que voulez vous faire ? ")
        possible_choices = ["0", "1", "2", "3", "4", "5"]
        c = None
        while c not in possible_choices:
            c = input("Choix : ")


        match c:
            case "1" :
                print("Hey")
            case _ :
                print("AAHAHAHHAHHA")