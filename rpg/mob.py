from abc import ABC, abstractmethod
from random import randint

from rpg.item import Item
from rpg.job import Job
from rpg.player import Player


class Mob(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def description(self):
        pass


class Npc(Mob):
    def __init__(self, name: str, job: Job, shop: list = None):
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
    def __init__(self, name: str, hp: int, damage: int, loot_table: dict[Item, dict[int, tuple[int, int]]]):
        super().__init__(name)
        self.hp = hp
        self.damage = damage
        self.loot_table = loot_table

    def description(self):
        print("=====MOB=====")
        print(f"{self.name} est hostile\nHP: {self.hp}\nDégât: {self.damage}" )
        print("=============")

    def attack(self, player: Player):
        if not player.is_dead():
            print(f"{self.name} attaque {player.name}")
            player.hp -= self.damage

    def is_dead(self):
        return self.hp <= 0

    def drop(self) -> list[Item]:
        drops = []

        for loot_item, prob_data in self.loot_table.items():
            for prob, (min_qty, max_qty) in prob_data.items():
                probability_index = randint(1, 100)
                if probability_index <= prob:
                    quantity = randint(min_qty, max_qty)
                    drops.append([loot_item, quantity])
        print(f"dropping {len(drops)} item(s)")
        for drop, quantity in drops:
            drop.display_item()
        return drops
