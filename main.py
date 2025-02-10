import pygame
import numpy as np
from track import Track
from vehicule_class import Vehicule

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Course avec IA et Pygame")
    clock = pygame.time.Clock()

    track = Track()
    vehicle = Vehicule(10, 0.3, np.linspace(-np.pi/5, np.pi/5, 20).tolist(), track.get_track()[0])

    car_image = pygame.image.load("assets/voiture.png").convert_alpha()
    car_image = pygame.transform.scale(car_image, (50, 80))

    font = pygame.font.Font(None, 36)
    start_time = pygame.time.get_ticks()

    key_state = {"left": False, "right": False, "up": False}
    running = True

    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Temps en secondes

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key_state["left"] = False
                if event.key == pygame.K_RIGHT:
                    key_state["right"] = False
                if event.key == pygame.K_UP:
                    key_state["up"] = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_state["left"] = True
                if event.key == pygame.K_RIGHT:
                    key_state["right"] = True
                if event.key == pygame.K_UP:
                    key_state["up"] = True

        if key_state["left"]:
            vehicle.setChamp('left')

        if key_state["right"]:
            vehicle.setChamp('right')

        if key_state["up"]:
            vehicle.accelerate()
        else:
            vehicle.decelerate()

        vehicle.setMoveAway()
        position = vehicle.getPosition()

        # Vérifier si la voiture est sur la route
        if not track.is_on_road(position[0], position[1]):
            vehicle.speed *= 0.5  # Ralentissement dans la boue

        # Vérifier si la voiture touche la ligne d'arrivée
        if np.linalg.norm(np.array(position) - np.array(track.get_track()[-1])) < 20:
            print(f"🏁 FIN DE COURSE ! Temps : {elapsed_time:.2f} secondes 🏁")
            running = False

        rotated_car = pygame.transform.rotate(car_image, -np.degrees(vehicle.getOrientation()))
        car_rect = rotated_car.get_rect(center=(position[0], position[1]))

        screen.fill((30, 30, 30))
        track.draw_track(screen)
        screen.blit(rotated_car, car_rect)

        time_text = font.render(f"Temps : {elapsed_time:.2f} s", True, (255, 255, 255))
        screen.blit(time_text, (50, 50))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
