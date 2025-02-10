import numpy as np
import random

class LSystemGenerator:
    def __init__(self, axiom="F", rules=None, iterations=5, step_size=40, angle_variation=25, road_width=120):
        self.axiom = axiom
        self.rules = rules if rules else {"F": "F-F+F+F-F"}  
        self.iterations = iterations
        self.step_size = step_size
        self.angle_variation = angle_variation
        self.road_width = road_width
        self.width_limit = 1280
        self.height_limit = 720

    def generate_sequence(self):
        """Génère la séquence de commandes du L-System."""
        axiom = self.axiom
        for _ in range(self.iterations):
            axiom = "".join(self.rules.get(c, c) for c in axiom)
        return axiom

    def generate_track(self):
        """Génère un tracé linéaire sans glitchs et avec un bon alignement."""
        x, y, direction = self.width_limit // 2, self.height_limit // 2, 0
        track = [(x, y)]
        last_dir = direction

        for cmd in self.generate_sequence():
            if cmd == "F":
                # Calcul de la prochaine position
                new_x = x + np.cos(np.radians(direction)) * self.step_size
                new_y = y + np.sin(np.radians(direction)) * self.step_size

                # Vérifier que la route ne sort pas des limites
                if 100 < new_x < self.width_limit - 100 and 100 < new_y < self.height_limit - 100:
                    # Corriger les angles trop serrés
                    if abs(direction - last_dir) > 90:
                        direction = (direction + last_dir) / 2  # Moyenne entre les angles
                    x, y = new_x, new_y
                    track.append((x, y))
                    last_dir = direction

            elif cmd == "+":
                direction += random.randint(5, self.angle_variation)  # Réduction de l’angle max
            elif cmd == "-":
                direction -= random.randint(5, self.angle_variation)

        return np.array(track)
