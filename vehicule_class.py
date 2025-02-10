import numpy as np

class Vehicule:
    """Classe qui gère la physique et le mouvement du véhicule."""

    def __init__(self, vit_max: int, acc: float, champ: list, position: list):
        """
        Initialise le véhicule.
        """
        self.speed = 0  # Démarre à l'arrêt
        self.max_speed = vit_max  # Vitesse max
        self.acceleration = acc  # Accélération progressive
        self.deceleration = 0.1  # Décélération naturelle
        self.friction = 0.05  # Perte de vitesse sur la boue
        self.vision = champ
        self.position = [position[0], position[1]]
        self.orientation = (champ[0] + champ[-1]) / 2
        self.maniability = np.pi / 20  # Plus faible pour éviter trop de virages brusques

    def accelerate(self):
        """Augmente progressivement la vitesse."""
        if self.speed < self.max_speed:
            self.speed += self.acceleration

    def decelerate(self):
        """Diminue la vitesse quand on lâche l'accélérateur."""
        if self.speed > 0:
            self.speed -= self.deceleration
        if self.speed < 0:
            self.speed = 0

    def apply_friction(self):
        """Applique un ralentissement si le véhicule est hors route."""
        if self.speed > 0:
            self.speed -= self.friction

    def setMoveAway(self):
        """Déplace le véhicule selon sa vitesse et son orientation."""
        self.position[0] += self.speed * np.cos(self.orientation)
        self.position[1] += self.speed * np.sin(self.orientation)

    def setChamp(self, direction: str):
        """Modifie l'orientation du véhicule."""
        if direction == 'right':
            self.orientation += self.maniability
        elif direction == 'left':
            self.orientation -= self.maniability

    def getPosition(self):
        return self.position

    def getOrientation(self):
        return self.orientation
