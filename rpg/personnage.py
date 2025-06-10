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
        adversaire.pdv -= self.att 
        
    def equipier(self, objet):
        self.inventaire.append(objet)

    def fiche_personnage(self):
        print("============")
        print(f"Nom: {self.nom}")
        print(f"Classe: {self.classe}")
        print(f"Vie: {self.pdv}")
        print(f"Attaque: {self.att}")
        print(f"Mana: {self.mana}")
        print(f"Inventaire: {self.inventaire}")
        print("============")

    @property
    def classe(self):
        return self.__class__.__name__.lower()

class Guerrier(Personnage):

    def __init__(self, nom, inventaire):
        super().__init__(nom, inventaire)
        self.att += 15
        
class Mage(Personnage):

    def __init__(self, nom, inventaire):
        super().__init__(nom, inventaire)
        self.att -= 10
        self.mana = 100