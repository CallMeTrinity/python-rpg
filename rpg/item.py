from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.value = value

    @abstractmethod
    def display_item(self):
        print("=====ITEM=====")
        print(f"{self.name}, vaut {self.value} pièces")


class Weapon(Item):
    type_item = "weapon"
    def __init__(self, name, att_boost, value = 0):
        super().__init__(name, value)
        self.att_boost = att_boost

    def display_item(self):
        super().display_item()
        print(f"{self.name} à un boost d'attaque de {self.att_boost}")
        print("============")

class Potion(Item):
    type_item = "potion"
    def __init__(self, name,  heal = 0, mana = 0, value = 0):
        super().__init__(name, value)
        self.heal = heal
        self.mana = mana

    def display_item(self):
        super().display_item()
        print(f"{self.name} offre {self.heal} soin et {self.mana} mana")
        print("============")