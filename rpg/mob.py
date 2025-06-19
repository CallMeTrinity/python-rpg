from abc import ABC, abstractmethod

from rpg.job import Job
from rpg.player import Player


class Mob(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def description(self):
        pass


class Npc(Mob):
    def __init__(self, name: str, job: Job, shop: list=None):
        super().__init__(name)
        self.job = job
        self.shop = shop

    def description(self):
        print(f"Pnj {self.name} est un {self.job.__name__}")

    def say(self, text):
        print(f"{self.name} dit : {text}")

    def show_shop(self):
        if self.job.seller:
            for item in self.shop:
                print("________")
                print(f"{item.display_item()}")
                if item.type_item == "potion":
                    print(f"soin: {item.heal}")
                    print(f"mana : {item.mana}")
                if item.type_item == "weapon":
                    print(f"Amélioration d'attaque: {item.att_boost}")
        else:
            print(f"{self.name} ne vend rien")

class Hostile(Mob):
    def __init__(self, name: str, pv: int , damage: int, loot_table: dict[str, int]):
        super().__init__(name)
        self.pv = pv
        self.damage = damage
        self.loot_table = loot_table
        self.dead = False

    def description(self):
        print(f"{self.name} est hostile")

    def attack(self, player: Player):
        if not player.is_dead():
            print(f"{self.name} attaque {player.name}")
            player.pv -= self.damage

    def is_dead(self):
        if self.pv <= 0:
            self.dead = True