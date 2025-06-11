class Objet:
    def __init__(self, nom):
        self.nom = nom

    def afficher_objet(self):
        print(f"Objet {self.nom}")


class Arme(Objet):
    type_objet = "arme"
    def __init__(self, nom, att_boost):
        super().__init__(nom)
        self.att_boost = att_boost

class Potion(Objet):
    type_objet = "potion"
    def __init__(self, nom, heal = 0, mana = 0):
        super().__init__(nom)
        self.heal = heal
        self.mana = mana