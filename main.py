import pygame
import numpy as np
from menu import Menu
from track import Track
from vehicule_class import Vehicule

def run_game(map_name, mode):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Course avec IA et Pygame")
    clock = pygame.time.Clock()

    # Charger la piste
    track = Track(map_name)

    # Initialisation du véhicule
    vehicle = Vehicule(10, 0.3, np.linspace(-np.pi/5, np.pi/5, 20).tolist(), track.get_track()[0])

    # Charger l’image du véhicule
    car_image = pygame.image.load("assets/voiture.png").convert_alpha()
    car_image = pygame.transform.scale(car_image, (50, 80))

    font = pygame.font.Font(None, 48)
    start_time = pygame.time.get_ticks()

    running = True

    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Temps en secondes

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vehicle.setChamp('left')
        if keys[pygame.K_RIGHT]:
            vehicle.setChamp('right')
        if keys[pygame.K_UP]:
            vehicle.accelerate()
        else:
            vehicle.decelerate()

        vehicle.setMoveAway()
        position = vehicle.getPosition()

        # Vérifier si la voiture est sur la route
        if not track.is_on_road(position[0], position[1]):
            vehicle.speed *= 0.5  # Ralentissement dans la boue

        # 🏁 Vérifier la collision avec la ligne d’arrivée
        finish_pos = track.finish_pos  # Position du drapeau
        if np.linalg.norm(np.array(position) - np.array(finish_pos)) < 40:  # Collision si distance < 40 px
            print(f"🏁 Course terminée ! Temps : {elapsed_time:.2f} secondes 🏁")
            running = False  # Arrêter la course

        screen.fill((30, 30, 30))
        track.draw_track(screen)

        # 💡 Rotation correcte du sprite en fonction de l'orientation
        rotated_car = pygame.transform.rotate(car_image, -np.degrees(vehicle.getOrientation()))
        car_rect = rotated_car.get_rect(center=(position[0], position[1]))
        screen.blit(rotated_car, car_rect)

        # 🕒 Affichage du chrono en couleur bien visible
        time_text = font.render(f"Temps : {elapsed_time:.2f} s", True, (0, 255, 0))
        screen.blit(time_text, (50, 50))

        pygame.display.flip()
        clock.tick(30)

    print("🏁 Fin du jeu 🏁")
    pygame.quit()

if __name__ == "__main__":
    screen = pygame.display.set_mode((1280, 720))
    pygame.init()
    menu = Menu(screen)
    selected_map, mode = menu.run()
    if selected_map:
        run_game(selected_map, mode)
