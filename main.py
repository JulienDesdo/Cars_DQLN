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
    car = Vehicule(1,1,0.,[np.linspace(0,np.pi,10)])
    Rect_car = pygame.Rect(100,540,50,30)
    Rect_Arrive = pygame.Rect(1100,50,50,50)

    while running==True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

             
        screen.fill("brown")
        pygame.draw.rect(screen,BLEU,Rect_car)
        pygame.draw.rect(screen,VERT,Rect_Arrive)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__" : 
    main()
