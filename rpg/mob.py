from abc import ABC, abstractmethod

from rpg.job import Job


class Mob(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def description(self):
        pass


class Npc(Mob):
    def __init__(self, name: str, job: Job, shop: dict=None):
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
                print(item.name)
                if item.type_item == "potion":
                    print(item.heal)
