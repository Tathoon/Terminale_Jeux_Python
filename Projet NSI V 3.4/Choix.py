import pygame
from Button import button

class choixBase:
    def __init__(self,mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/mainBack01.jpg'),(mainScreen.get_size()))
        self.buttonChoixA = button("assets/choice/choixA.jpg", 200, 400, 450, mainScreen.get_height()-400)
        self.buttonChoixB = button("assets/choice/choixB.jpg", 200, 400, mainScreen.get_width()-450, mainScreen.get_height()-400)
        
    def update(self, mainScreen, background):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonChoixA.image,self.buttonChoixA.rect)
        mainScreen.blit(self.buttonChoixB.image,self.buttonChoixB.rect)
