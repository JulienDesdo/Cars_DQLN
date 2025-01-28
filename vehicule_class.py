

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
        self.position = [0,0]

    def setSpeed(self,ns:int):

        self.speed = ns

    def setOrientation(self,no:int):
        """Upgrade variable Orientation with a new value"""
        self.orientation = no
        
    def setSpeed(self,nv:int):
        """Upgrade variable Vision with a new value"""
        self.speed = nv

    def setPositionX(self):
        """Upgrade variable X axe Position with a new value"""
        self.position[0] = self.speed + self.position[0]

    def setPositionX(self):
        """Upgrade variable Y axes Position with a new value"""
        self.position[1] = self.speed + self.position[1]






