from rpg.exception import WeaponAlreadyEquippedException, UnauthorizedActionException, InventoryFullException


class Personnage:
    """
    string nom
    string[] inventaire
    int pdv
    int att
    """

    def __init__(self, nom, inventaire):
        self.nom = nom
        self.inventaire = inventaire
        self.pdv = 100
        self.att = 25
        self.mana = 0
        self.hand = None

    def attaquer(self, adversaire):
        if self.est_mort():
            raise UnauthorizedActionException(f"{self.nom} est mort il ne peut pas attaquer")
        print(f"{self.nom} attaque {adversaire.nom}")
        if self.hand is not None:
            self.att += self.hand.att_boost
            print(f"{self.nom} utilise {self.hand.nom} et obtient un bonus d'attaque de {self.hand.att_boost}")
        adversaire.pdv -= self.att
        if adversaire.est_mort():
            print(f"{adversaire.nom} est mort")
        else:
            print(f"{adversaire.nom} a {adversaire.pdv} PV restant")



    def equiper(self, objet):
        for el in self.inventaire:
            if objet.nom == el.nom and self.hand is None:
                self.hand = el
                self.inventaire.remove(el)
            else:
                raise UnauthorizedActionException(f"Cet objet n'est pas dans votre inventaire : {objet.nom}")


    def ranger(self, objet):
        if self.hand is not None:
            self.inventaire.append(objet)
            self.hand = None
        else:
            UnauthorizedActionException("Vous n'avez rien dans votre main")


    def stash(self, objet):
        if len(self.inventaire) < 6:
            self.inventaire.append(objet)
        else:
            raise InventoryFullException

    def fiche_personnage(self):
        print("============")
        print(f"Nom: {self.nom}")
        print(f"Classe: {self.classe}")
        print(f"Vie: {self.pdv}")
        print(f"Attaque: {self.att}")
        print(f"Mana: {self.mana}")
        print("Inventaire:")
        for objet in self.inventaire:
            print(f"--Nom: {objet.nom}")
            print(f"----Type: {objet.type_objet}")
            if objet.type_objet == "arme":
                print(f"----Bonus d'attaque: +{objet.att_boost}")
            elif objet.type_objet == "potion":
                print(f"----Bonus de soin: +{objet.heal}")
                print(f"----Bonus de mana: +{objet.mana}")
        if self.hand is not None:
            print(f"Main: {self.hand.nom}")
        print("============")

    @property
    def classe(self):
        return self.__class__.__name__.lower()

    def est_mort(self):
        return self.pdv <= 0

class Guerrier(Personnage):

    def __init__(self, nom, inventaire):
        super().__init__(nom, inventaire)
        self.att += 15


class Mage(Personnage):

    def __init__(self, nom, inventaire):
        super().__init__(nom, inventaire)
        self.att -= 10
        self.mana = 100
