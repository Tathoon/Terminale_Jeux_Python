# Importation de Pygame et chargement de ses composants
import pygame
from pygame.locals import *
pygame.init()

class player:

    def __init__(self):
        self.health = 1
        self.max_health = 1
        """à suivre"""
    











mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1000, 650)) # Création et définition des dimmensions de la fenêtre

# Import de l'arrière plan
background = pygame.image.load('Assets/test.png')

# Boucle qui permet la fermeture de la fenêtre lorsque la croix est pressee
running = True
while running:

    # appliquer l'arrière plan puis mettre à jour la fenêtre

    mainScreen.blit(background, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
