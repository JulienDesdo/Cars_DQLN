"""
    Type de commentaire pour docstrings.  
"""
# Génération d'une documentation : Sphynx & Docstrings (à regarder)
'''
Install l'extension PythonDocsString Generator si sous VScode.
https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

Sinon,
pip install sphinx 
sphinx-quickstart
extensions = ['sphinx.ext.autodoc'] (inclusion des docsstrings, configuration de conf.py)
makehtml
'''

import pygame
# from module import MyClass
from vehicule_class import Vehicule
import numpy as np
import os

class Carte:
    """Exemple de classe dans module1.py."""

    def __init__(self, size: list):
        
        self.size =  size

    def method(self):
        """Affiche un message avec le nom."""
        print(f"Hello from {self.name} in MyClass1!")

    def get_size(self):
        return self.size


def main():
    '''Point d'entrée principal du programme.'''
    # mon_obj = MyClass()

    print("Start programme !")

    pygame.init()
    
    BLEU = (0,0,150)
    VERT = (0,150,0)

    carte = Carte((1280,720))
    screen = pygame.display.set_mode(carte.get_size())
    clock = pygame.time.Clock()

    start_time = pygame.time.get_ticks()  # Temps de départ
    font = pygame.font.Font(None, 36)
    finish_time = start_time
    journal_file = "journal_temps.txt"

    running = True

    champ=list(np.linspace(-np.pi/5,np.pi/5,20))
    car = Vehicule(10,1,champ,[100,540])
    key_state = {
        "left":False,
        "right":False,
        "up":False,
        "down":False
    }


    position = car.getPosition()
    car_image_base = pygame.image.load("voiture.png")
    car_image_base = pygame.transform.scale(car_image_base,(30,50))
    car_image = pygame.transform.rotate(car_image_base,-90)
    Rect_car = car_image.get_rect(center=(position[0],position[1]))
    lock_RectCar = True


    terminus_image = pygame.image.load("terminus_line.png")
    terminus_image = pygame.transform.scale(terminus_image,(50,50))
    Rect_Arrive = terminus_image.get_rect(center=(1100,50))


    while running==True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            elif event.type == pygame.KEYUP:
        
                if event.key == pygame.K_UP:
                    key_state["up"] = False
            
                if event.key == pygame.K_LEFT:
                    key_state["left"] = False
                    
                if event.key == pygame.K_RIGHT:
                    key_state["right"] = False


            elif event.type == pygame.KEYDOWN:
        
                if event.key == pygame.K_UP:
                    key_state["up"] = True

                if event.key == pygame.K_LEFT:
                    key_state["left"] = True
                    
                if event.key == pygame.K_RIGHT:
                    key_state["right"] = True
        

        if key_state["left"]:
            old_dir = car.getOrientation()
            car.setChamp('left',old_dir)

        if key_state["right"]:
            old_dir = car.getOrientation()
            car.setChamp('right',old_dir)


        if key_state["up"]:
                    car.setMoveAway()
                    position = car.getPosition()
                    Rect_car.center=(position[0],position[1])
        
        
        if Rect_Arrive.colliderect(Rect_car):
            lock_RectCar = False
            finish_time = elapsed_time

            if os.path.exists(journal_file):
                with open(journal_file, "a") as file:
                    file.write(f"{elapsed_time}\n")
                print("Historique des temps :")
                with open(journal_file, "r") as file:
                    contenu = file.read()
                    record_time = [contenu[0:6],contenu[8:13],contenu[15:20],contenu[22:27],contenu[29:33]]

                    print(contenu if contenu else "Aucun temps enregistré.")
                    
            else:
                print(f"Le fichier {journal_file} n'existe pas encore. Il sera créé à la fermeture.")
                with open(journal_file, "a") as file:
                    file.write(f"{elapsed_time}\n")
                print(f"Temps enregistré : {elapsed_time} ms")


            running = False

        
        elapsed_time = pygame.time.get_ticks() - start_time
        elapsed_text = font.render(f"Temps : {elapsed_time} ms", True, (255, 255, 255))

        screen.fill("brown")
        
        screen.blit(terminus_image,Rect_Arrive)

        if lock_RectCar:
            screen.blit(car_image,Rect_car)
            screen.blit(elapsed_text, (50, 50))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__" : 
    main()
