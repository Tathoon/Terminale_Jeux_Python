import pygame
from Button import button

class menu:
    def __init__(self, mainScreen):
        self.is_active = True
        # Importation de l'arrière plan
        self.background = pygame.transform.scale(pygame.image.load('assets/background/mainBack01.jpg'),(mainScreen.get_size()))
        #Création d'un bouton Start
        self.buttonStart = button("assets/button/startbutton02.png", 305, 135, 395, 460)

    def update(self, mainScreen, background):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonStart.image,self.buttonStart.rect)