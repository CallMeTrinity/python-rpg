class Pnj:

    neutral_types = ["villageois", "vendeur", "Prêtre", "Noble"]
    hostile_types = ["pillard", "ghoul"]

    def __init__(self, nom: str, type: str,  hostile: bool) -> None:
        self.nom = nom
        self.type = type
        self.pdv = 50
        self.hostile = hostile
        self.estMort = False



    def presentation(self):
        if not self.estMort:
            print(f"Je suis {self.nom}")
            if self.hostile:
                print("Grr")
            else:
                print(":)")


class Villageois(Pnj):
    def __init__(self, nom: str, type: str = "nitwit") -> None:
        super().__init__(nom, type, False)

    def fuir(self):
        if not self.estMort:
            if self.pdv < 15:
                print(f"{self.nom} prend la fuite")

class Monstre(Pnj):
    def __init__(self, nom: str, type: str = "ghoul") -> None:
        super().__init__(nom, type, True)

    def attaquer(self, joueur):
        print(f"{self.nom} attaque {joueur.nom}")
        joueur.pdv -= 10