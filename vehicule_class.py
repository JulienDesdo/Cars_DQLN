

class Vehicule:
    """Class Véhicule qui va manipuler l'ensemble du véhicule."""

    def __init__(self, vit: int,acc: int, orientation:float, Champ:list):
        """
        Initialise l'instance de la classe.
        """
        self.speed = vit
        self.acceleration = acc
        self.orientation = orientation
        self.vision = Champ

    def upgradeSpeed(self,ns:int):
        """Upgrade variable Speed with a new value"""
        self.speed = ns


    def upgradeOrientation(self,no:int):
        """Upgrade variable Orientation with a new value"""
        self.orientation = no
        
    def upgradeVision(self,nv:int):
        """Upgrade variable Vision with a new value"""
        self.speed = nv







