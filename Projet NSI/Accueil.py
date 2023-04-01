import pygame

class accueil:
    def __init__(self,mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuBack01.jpg'),(mainScreen.get_size()))

    def update(self, mainScreen, background):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        