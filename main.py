import pygame
import numpy as np
import os
from menu import Menu
from track import Track
from vehicule_class import Vehicule
from train_agent import train_model
from test_agent import test_model

MODEL_PATH = "racing_agent.zip"

def run_game(map_name, mode, show_vision):
    """Lance le jeu selon le mode sélectionné dans le menu."""
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Course avec IA et Pygame")
    clock = pygame.time.Clock()

    # -- Mode ENTRAÎNEMENT
    if mode == "ENTRAÎNEMENT":
        pygame.quit()  # On ferme la fenêtre du menu
        train_model(map_name)
        return

    # -- Mode TEST
    if mode == "TEST":
        if not os.path.exists(MODEL_PATH):
            print("❌ Erreur : Modèle 'racing_agent.zip' introuvable !")
            return
        # NE PAS quitter pygame ici, on veut charger des images
        test_model(map_name, show_vision)
        pygame.quit()
        return

    # -- Mode NORMAL (Joueur ou IA)
    # On veut afficher la piste => with_images=True
    track = Track(map_name, with_images=True)
    vision_active = (mode == "IA")
    vehicle = Vehicule(vit_max=10, acc=0.3, position=track.get_track()[0], vision_active=vision_active)

    # Charger le sprite de la voiture
    car_image = pygame.image.load("assets/voiture.png").convert_alpha()
    car_image = pygame.transform.scale(car_image, (50, 80))

    font = pygame.font.Font(None, 48)
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Contrôles du joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vehicle.setChamp('left')
        if keys[pygame.K_RIGHT]:
            vehicle.setChamp('right')
        if keys[pygame.K_UP]:
            vehicle.accelerate()
        else:
            vehicle.decelerate()

        # Déplacement
        vehicle.setMoveAway()
        position = vehicle.getPosition()

        # Hors piste => ralentit
        if not track.is_on_road(position[0], position[1]):
            vehicle.speed *= 0.5

        # Collision ligne d'arrivée => stop
        dist_finish = np.linalg.norm(np.array(position) - np.array(track.finish_pos))
        if dist_finish < 40:
            print("🚩 Course terminée !")
            running = False

        # -- Affichage
        screen.fill((30, 30, 30))
        track.draw_track(screen)

        # Rotation (offset +90 si la voiture pointe vers le haut dans le .png)
        offset_angle = 90
        angle_deg = -np.degrees(vehicle.getOrientation()) + offset_angle
        rotated_car = pygame.transform.rotate(car_image, angle_deg)
        rect_car = rotated_car.get_rect(center=(position[0], position[1]))
        screen.blit(rotated_car, rect_car)

        # Dessin des rayons IA si demandé
        if show_vision:
            vehicle.draw_vision(screen, track)

        # Chrono
        txt = font.render(f"Temps : {elapsed_time:.2f} s", True, (0, 255, 0))
        screen.blit(txt, (50, 50))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    menu = Menu(screen)

    print("🎮 Affichage du menu Pygame...")
    selected_map, mode, show_vision = menu.run()

    if selected_map:
        print(f"✅ Menu sélectionné : {mode} sur {selected_map}")
        run_game(selected_map, mode, show_vision)
    else:
        print("🔴 Fermeture du programme (aucune sélection faite).")
