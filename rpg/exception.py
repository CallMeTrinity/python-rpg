class WeaponAlreadyEquippedException(Exception):
    def __init__(self, message="Un objet de type arme est déjà équippé dans votre inventaire", *args):
        super().__init__(message, *args)

class UnauthorizedActionException(Exception):
    def __init__(self, message="Un personnage essaie d'effectuer une action non autorisé", *args):
        super().__init__(message, *args)

class InventoryFullException(Exception):
    def __init__(self, message="L'inventaire est déjà plein", *args):
        super().__init__(message, *args)