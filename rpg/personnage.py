from rpg.exception import WeaponAlreadyEquippedException, UnauthorizedActionException


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

    def attaquer(self, adversaire):
        if self.est_mort():
            raise UnauthorizedActionException(f"{self.nom} est mort il ne peut pas attaquer")
        print(f"{self.nom} attaque {adversaire.nom}")
        if len(self.inventaire) > 0:
            for objet in self.inventaire:
                if objet.type_objet == "arme":
                    self.att += objet.att_boost
                    print(f"{self.nom} utilise {objet.nom} et obtient un bonus d'attaque de {objet.att_boost}")
                    break
        adversaire.pdv -= self.att
        if adversaire.est_mort():
            print(f"{adversaire.nom} est mort")
        else:
            print(f"{adversaire.nom} a {adversaire.pdv} PV restant")



    def equiper(self, objet):
        if objet.type_objet == "arme":
            for objet in self.inventaire:
                if objet.type_objet == "arme":
                    raise WeaponAlreadyEquippedException()
                else:
                    self.inventaire.append(objet)
            else:
                self.inventaire.append(objet)

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
