class WeaponAlreadyEquippedException(Exception):
    def __init__(self, message="Un item de type arme est déjà équippé dans votre inventory", *args):
        super().__init__(message, *args)

class UnauthorizedActionException(Exception):
    def __init__(self, message="Un personnage essaie d'effectuer une action non autorisé", *args):
        super().__init__(message, *args)

class InventoryFullException(Exception):
    def __init__(self, message="L'inventory est déjà plein", *args):
        super().__init__(message, *args)
class InvalidTypeException(Exception):
    def __init__(self, message="Le type est non reconnu", *args):
        super().__init__(message, *args)