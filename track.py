import pygame
import numpy as np
import random

class Track:
    def __init__(self, map_name):
        self.road_width = 120  # Largeur de la route

        # 🏁 Cartes fixes (listes de points définies à la main)
        if map_name == "Map 1":
            self.track = [(100, 300), (300, 300), (500, 500), (700, 500), (900, 300), (1100, 300)]
        elif map_name == "Map 2":
            self.track = [(100, 600), (300, 400), (500, 300), (700, 400), (900, 500), (1100, 600)]
        elif map_name == "Map 3":
            self.track = [(200, 200), (400, 300), (600, 400), (800, 500), (1000, 400), (1200, 300)]
        else:
            # Génération procédurale avec L-System
            from l_system import LSystemGenerator
            self.generator = LSystemGenerator()
            self.track = self.generator.generate_track().tolist()

        # Surface pour stocker la route
        self.road_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.road_surface.fill((0, 0, 0, 0))

        # Dessiner la route
        for i in range(len(self.track) - 1):
            pygame.draw.line(self.road_surface, (255, 255, 255, 255), self.track[i], self.track[i + 1], self.road_width)

        # Ligne d'arrivée à la fin du circuit
        self.finish_image = pygame.image.load("assets/terminus_line.png").convert_alpha()
        self.finish_image = pygame.transform.scale(self.finish_image, (80, 40))
        self.finish_pos = self.track[-1]

    def draw_track(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.road_surface, (0, 0))

        # Afficher la ligne d’arrivée
        screen.blit(self.finish_image, (self.finish_pos[0] - 40, self.finish_pos[1] - 20))

    def is_on_road(self, x, y):
        """Retourne True si la voiture est sur la route."""
        if 0 <= x < 1280 and 0 <= y < 720:
            return self.road_surface.get_at((int(x), int(y)))[0] > 0
        return False

    def get_track(self):
        return self.track
