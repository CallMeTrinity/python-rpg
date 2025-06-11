from rpg.exception import UnauthorizedActionException
from rpg.objet import Arme
from rpg.personnage import Guerrier


def main():

    master_sword = Arme("Master Sword", att_boost=20)

    moi = Guerrier("Antonin", [])
    moi.equiper(master_sword)
    moi.fiche_personnage()

    adversaire = Guerrier("Adversaire", [])
    adversaire.fiche_personnage()

    moi.attaquer(adversaire)
    moi.attaquer(adversaire)

    try:
        adversaire.attaquer(moi)
    except UnauthorizedActionException as e:
        print(e)
if __name__ == "__main__":
    main()