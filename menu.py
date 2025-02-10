import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.options = ["Map 1", "Map 2", "Map 3", "L-System", "Quitter"]
        self.modes = ["Joueur", "IA"]
        self.selected_map = 0
        self.selected_mode = 0

    def draw(self):
        self.screen.fill((20, 20, 20))
        
        title = self.font.render("Sélectionner une carte", True, (200, 200, 200))
        self.screen.blit(title, (500, 50))

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_map else (255, 255, 255)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (550, 150 + i * 60))

        mode_title = self.font.render("Mode de jeu", True, (200, 200, 200))
        self.screen.blit(mode_title, (500, 500))

        for i, mode in enumerate(self.modes):
            color = (255, 255, 0) if i == self.selected_mode else (255, 255, 255)
            text = self.font.render(mode, True, color)
            self.screen.blit(text, (600, 550 + i * 60))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None, None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_map = (self.selected_map - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_map = (self.selected_map + 1) % len(self.options)
                    elif event.key == pygame.K_LEFT:
                        self.selected_mode = (self.selected_mode - 1) % len(self.modes)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_mode = (self.selected_mode + 1) % len(self.modes)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_map] == "Quitter":
                            return None, None
                        return self.options[self.selected_map], self.modes[self.selected_mode]
