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
        ax = self.axiom
        for _ in range(self.iterations):
            ax = "".join(self.rules.get(c, c) for c in ax)
        return ax

    def generate_track(self):
        x, y = self.width_limit // 2, self.height_limit // 2
        direction = 0
        track = [(x, y)]
        last_dir = direction

        seq = self.generate_sequence()
        for cmd in seq:
            if cmd == "F":
                new_x = x + np.cos(np.radians(direction)) * self.step_size
                new_y = y + np.sin(np.radians(direction)) * self.step_size
                if 100 < new_x < self.width_limit - 100 and 100 < new_y < self.height_limit - 100:
                    if abs(direction - last_dir) > 90:
                        direction = (direction + last_dir) / 2
                    x, y = new_x, new_y
                    track.append((x, y))
                    last_dir = direction
            elif cmd == "+":
                direction += random.randint(5, self.angle_variation)
            elif cmd == "-":
                direction -= random.randint(5, self.angle_variation)

        return np.array(track)
