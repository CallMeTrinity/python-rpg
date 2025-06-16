from rpg.exception import UnauthorizedActionException
from rpg.objet import Arme
from rpg.personnage import Guerrier
from rpg.jeu import Jeu

def main():

    n = input("Combien de joueurs sont présents ? ")
    Jeu(int(n))

if __name__ == "__main__":
    main()