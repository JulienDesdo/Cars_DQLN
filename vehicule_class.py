import numpy as np

class Vehicule:
    """Class Véhicule qui va manipuler l'ensemble du véhicule."""

    def __init__(self, vit: int,acc: int, Champ:list,position:list):
        """
        Initialise l'instance de la classe.
        """
        self.speed = vit
        self.acceleration = acc
        self.vision = Champ
        self.position = [position[0],position[1]]
        self.orientation = (Champ[0] + Champ[-1]) / 2
        self.maniability = np.pi/8

    def setSpeed(self,ns:int):

        self.speed = ns

    def setOrientation(self,no:float):
        """Upgrade variable Orientation with a new value"""
        self.orientation = no
        
    def setSpeed(self,nv:int):
        """Upgrade variable Vision with a new value"""
        self.speed = nv

    def setMoveAway(self):
        """Upgrade variable X axe Position with a new value"""
        self.position[0] += self.speed * np.cos(self.orientation)
        self.position[1] += self.speed * np.sin(self.orientation)
        
    def setChamp(self,val:str):

        if val == 'right':
            for i in range(len(self.vision)):

                if self.vision[i]+self.maniability > np.pi :
                    self.vision[i] += self.maniability - 2 * np.pi
                else:
                    self.vision[i] += self.maniability

        elif val == 'left':
            for i in range(len(self.vision)):
                if self.vision[i]-self.maniability < -np.pi :
                    self.vision[i] -= self.maniability + 2 * np.pi
                else:
                    self.vision[i] -= self.maniability

        else:
            print("ERROR! Director of variable change not define")

        vec_dir = (self.vision[0] + self.vision[-1]) / 2
        self.setOrientation(vec_dir)

    def getPosition(self):
        return self.position

    def getOrientation(self):
        return self.orientation



