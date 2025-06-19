from random import randint

from rpg.exception import InvalidTypeException
from rpg.item import Weapon, Potion
from rpg.player import Wizard, Barbarian


class Game:
    classes = ['wizard', 'barbarian']
    players = {}
    items = []

    def __init__(self, player_count):
        self.player_count = player_count
        self.init_players()
        self.init_items()

    def create_player(self, c, name, inventory=None):
        if inventory is None:
            inventory = []
        match c:
            case "barbarian":
                new_player = Barbarian(name, inventory)
            case "wizard":
                new_player = Wizard(name, inventory)
            case _:
                raise InvalidTypeException(f"La classe : '{c}' n'existe pas.")
        self.players[name] = new_player

    def init_players(self):
        for i in range(self.player_count):
            print(f"création du joueur {i + 1}")
            name = input(f"Quel est le name du joueur n°{i + 1} ")
            print(f"Classes de personnages disponibles : {self.classes}")
            classe = None
            while classe not in self.classes:
                classe = input(f"Selectionnez la classe de votre personnage : ")
            self.create_player(classe, name)

    def init_items(self):
        nb_items = 4 * self.player_count
        for i in range(randint(2, nb_items)):
            if i + 1 <= round(0.5 * nb_items):
                self.items.append(Weapon(f"Arme-{i}", randint(10, 30)))
            else:
                self.items.append(Potion(f"Potion-{i}", randint(10, 30), randint(25, 50)))
