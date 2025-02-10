import pygame
from l_system import LSystemGenerator

class Track:
    def __init__(self):
        self.generator = LSystemGenerator()
        self.track = self.generator.generate_track()
        self.road_width = 120  # Largeur de route

        # Charger l'image du drapeau d'arrivée
        self.finish_image = pygame.image.load("assets/terminus_line.png").convert_alpha()
        self.finish_image = pygame.transform.scale(self.finish_image, (80, 40))

        # Création d'une surface pour stocker la route
        self.road_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.road_surface.fill((0, 0, 0, 0))

        # Dessiner la route SANS TROUS
        for i in range(len(self.track) - 1):
            pygame.draw.line(self.road_surface, (255, 255, 255, 255), self.track[i], self.track[i + 1], self.road_width)

    def draw_track(self, screen):
        screen.fill((30, 30, 30))  # Fond sombre
        screen.blit(self.road_surface, (0, 0))

        # Placer la ligne d’arrivée correctement
        finish_pos = self.track[-1]
        screen.blit(self.finish_image, (finish_pos[0] - 40, finish_pos[1] - 20))

    def is_on_road(self, x, y):
        """Retourne True si la voiture est sur la route."""
        if 0 <= x < 1280 and 0 <= y < 720:
            return self.road_surface.get_at((int(x), int(y)))[0] > 0
        return False

    def get_track(self):
        return self.track
