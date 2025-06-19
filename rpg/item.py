class Item:
    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.value = value

    def display_item(self):
        print(f"item {self.name}, vaut {self.value} pièces")


class Weapon(Item):
    type_item = "weapon"
    def __init__(self, name, att_boost, value = 0):
        super().__init__(name, value)
        self.att_boost = att_boost

class Potion(Item):
    type_item = "potion"
    def __init__(self, name,  heal = 0, mana = 0, value = 0):
        super().__init__(name, value)
        self.heal = heal
        self.mana = mana