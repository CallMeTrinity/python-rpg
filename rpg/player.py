from rpg.exception import WeaponAlreadyEquippedException, UnauthorizedActionException, InventoryFullException


class Player:

    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.hp = 100
        self.att = 25
        self.mana = 0
        self.gold = 0
        self.hand = None
        self.followed_quest = None
        self.xp = 0
        self.level = 1

    def attack(self, enemy):
        if self.is_dead():
            raise UnauthorizedActionException(f"{self.name} est mort il ne peut pas attaquer")
        print(f"{self.name} attaque {enemy.name}")
        if self.hand is not None:
            self.att += self.hand.att_boost
            print(f"{self.name} utilise {self.hand.name} et obtient un bonus d'attaque de {self.hand.att_boost}")
        enemy.hp -= self.att
        if enemy.is_dead():
            print(f"{enemy.name} est mort")
        else:
            print(f"{enemy.name} a {enemy.hp} hp restant")



    def equip(self, item):
        for el in self.inventory:
            if item.name == el.name and self.hand is None:
                self.hand = el
                self.inventory.remove(el)
            else:
                raise UnauthorizedActionException(f"Cet item n'est pas dans votre inventory : {item.name}")


    def store(self, item):
        if self.hand is not None:
            self.inventory.append(item)
            self.hand = None
        else:
            UnauthorizedActionException("Vous n'avez rien dans votre main")


    def stash(self, item):
        if len(self.inventory) < 6:
            self.inventory.append(item)
        else:
            raise InventoryFullException

    def player_sheet(self):
        print("=====PLAYER=====")
        print(f"name: {self.name}")
        print(f"Classe: {self.classe}")
        print(f"Niveau: {self.level}")
        print(f"XP: {self.xp}")
        print(f"Or: {self.gold}")
        print(f"Vie: {self.hp}")
        print(f"Attaque: {self.att}")
        print(f"Mana: {self.mana}")
        print("inventory:")
        for item in self.inventory:
            print(f"--name: {item.name}")
            print(f"----Type: {item.type_item}")
            if item.type_item == "arme":
                print(f"----Bonus d'attaque: +{item.att_boost}")
            elif item.type_item == "potion":
                print(f"----Bonus de soin: +{item.heal}")
                print(f"----Bonus de mana: +{item.mana}")
        if self.hand is not None:
            print(f"Main: {self.hand.name}")
        print("============")

    def buy(self, item, seller):
        if self.gold >= item.value:
            self.gold -= item.value
            seller.shop.remove(item)

    @property
    def classe(self):
        return self.__class__.__name__.lower()

    def is_dead(self):
        return self.hp <= 0

    def follow_quest(self, quest):
        self.followed_quest = quest

    def start_followed_quest(self):
        if self.followed_quest is not None:
            self.followed_quest.start()
        else:
            print("Vous ne suivez aucune quête")

    def add_xp(self, xp: int):
        if self.xp + xp >= 100:
            self.xp += xp
            self.xp %= 100
            self.level += 1
            print(f"⭐Niveau {self.level - 1} -> {self.level} ⭐")
        else:
            self.xp += xp
        print(f"Vous avez gagné {xp} point d'xp et vous êtes niveau {self.level}")


class Barbarian(Player):

    def __init__(self, name, inventory):
        super().__init__(name, inventory)
        self.att += 15


class Wizard(Player):

    def __init__(self, name, inventory):
        super().__init__(name, inventory)
        self.att -= 10
        self.mana = 100
