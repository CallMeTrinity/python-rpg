from random import randint
from time import sleep

from rpg.exception import InvalidTypeException
from rpg.item import Weapon, Potion
from rpg.job import Job
from rpg.mob import Hostile, Npc
from rpg.player import Wizard, Barbarian
from rpg.quest import DialogQuest
from rpg.turn import Turn

class Game:


    def __init__(self, player_count):
        self.classes = ['wizard', 'barbarian']
        self.players = {}
        self.items = []
        self.hostiles = []
        self.player_names = []
        self.player_count = player_count

        self.init_players()
        self.init_items()
        self.init_mobs()

        turn = Turn(self.players)
        turn.play()
        # self.play()


    def play(self):
        for player in self.players:
            self.player_names.append(self.players[player].name)
            print(self.players[player].player_sheet())
            sleep(1)

        z = self.hostiles[0]
        z.description()
        sleep(1)
        while not z.is_dead():
            self.players[self.player_names[0]].attack(z)
        dropped_items = z.drop()
        sleep(1)
        quest = DialogQuest("Test", "Une quête de test","Bravo vous avez finis la quête !", "Sens de la vie ?", ["41", "42"], 2)
        job = Job("Villageois", False)
        npc = Npc("Roger", job, None, quest)

        npc.give_quest(self.players[self.player_names[0]])
        self.players[self.player_names[0]].start_followed_quest()
        if self.players[self.player_names[0]].followed_quest.completed:
            self.players[self.player_names[0]].followed_quest.reward(self.players[self.player_names[0]],150, 10)
        self.players[self.player_names[0]].player_sheet()

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
                random_damage_boost = randint(10, 30)
                if random_damage_boost > 20:
                    random_value = randint(15, 30)
                else:
                    random_value = randint(5, 15)
                self.items.append(Weapon(f"Arme-{i}", random_damage_boost, random_value))
            else:
                random_heath = randint(10, 30)
                random_mana = randint(25, 50)
                if random_heath > 20:
                    random_value = randint(10, random_heath)
                elif random_mana > 35:
                    random_value = randint(20, random_mana)
                else:
                    random_value = 0
                self.items.append(Potion(f"Potion-{i}", random_heath, random_mana, random_value))

    def init_mobs(self):
        for i in range(10):
            z = self.create_hostile('zombie')
            self.hostiles.append(z)

    def create_hostile(self, name):
        mob = Hostile(name, 100, 10,{self.items[1]: {100: (1,1)}})
        return mob
