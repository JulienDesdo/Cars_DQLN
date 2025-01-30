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
    running = True

    car_image = pygame.image.load("voiture.png")
    car_image = pygame.transform.scale(car_image,(30,50))
    car_image = pygame.transform.rotate(car_image,-90)
    
    champ=list(np.linspace(-np.pi/4,np.pi/4,20))
    car = Vehicule(2,1,champ,[100,540])
    key_state = {
        "left":False,
        "right":False,
        "up":False,
        "down":False
    }
    
    
    Rect_car = car_image.get_rect(center=(100,580))
    Rect_Arrive = pygame.Rect(1100,50,50,50)


    while running==True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            elif event.type == pygame.KEYUP:
        
                if event.key == pygame.K_UP:
                    key_state["up"] = False

                if event.key == pygame.K_LEFT:
                    key_state["up"] = False
                if event.key == pygame.K_RIGHT:
                    key_state["up"] = False
            
            elif event.type == pygame.KEYDOWN:
        
                if event.key == pygame.K_UP:
                    key_state["up"] = True

                if event.key == pygame.K_LEFT:
                    key_state["up"] = True
                    angle = car.getOrientation()
                    car_image = pygame.transform.rotate(car_image,-0.1)
                    car.setChamp(-0.1)
                    Rect_car = car_image.get_rect(top=(100,580))
                    
                if event.key == pygame.K_RIGHT:
                    key_state["up"] = True
                    angle = car.getOrientation()
                    car_image = pygame.transform.rotate(car_image,0.1)
                    car.setChamp(0.1)
                    Rect_car = car_image.get_rect(center=(100,580))
        
        if key_state["up"]:
                    print('appuie !')
                    car.setMoveAway()
                    position = car.position
                    Rect_car.x = position[0]
                    Rect_car.y = position[1]
        #elif key_state["left"]:
            
        #elif key_state["right"]:
            

        

        screen.fill("brown")
        screen.blit(car_image,Rect_car)
        pygame.draw.rect(screen,VERT,Rect_Arrive)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__" : 
    main()
