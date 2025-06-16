from random import randint

from rpg.exception import InvalidTypeException
from rpg.objet import Arme, Potion
from rpg.personnage import Guerrier, Mage


class Jeu:
    classes = ['guerrier', 'mage']
    joueurs = {}
    objets = []

    def __init__(self, nb_joueur):
        self.nb_joueur = nb_joueur
        self.init_players(nb_joueur)
        self.init_objets()

    def create_player(self, c, nom, inventaire=None):
        if inventaire is None:
            inventaire = []
        match c:
            case "guerrier":
                new_player = Guerrier(nom, inventaire)
            case "mage":
                new_player = Mage(nom, inventaire)
            case _:
                raise InvalidTypeException(f"La classe : '{c}' n'existe pas.")
        self.joueurs[nom] = new_player

    def init_players(self, nb_joueur):
        for i in range(nb_joueur):
            print(f"création du joueur {i + 1}")
            nom = input(f"Quel est le nom du joueur n°{i + 1} ")
            print(f"Classes de personnages disponibles : {self.classes}")
            classe = None
            while classe not in self.classes:
                classe = input(f"Selectionnez la classe de votre personnage : ")
            self.create_player(classe, nom)

    def init_objets(self):
        nb_objets = 4 * self.nb_joueur
        for i in range(randint(2, nb_objets)):
            if i + 1 <= round(0.5 * nb_objets):
                self.objets.append(Arme(f"Arme-{i}", randint(10, 30)))
            else:
                self.objets.append(Potion(f"Potion-{i}", randint(10, 30), randint(25, 50)))
