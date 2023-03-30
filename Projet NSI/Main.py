# Importation de Pygame et chargement de ses composants
import pygame
from pygame.locals import *
pygame.init()

# Importation de la classe button du fichier Button.py
from Button import button


# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

# Importation de l'arrière plan
background = pygame.image.load('assets/background/mainBack01.jpg')
background = pygame.transform.scale(background,(mainScreen.get_size()))

#Création d'un bouton Start
buttonStart = button("assets/button/startbutton02.png", 305, 135, 395, 460)

# Boucle du jeu
running = True
while running:

    # ajour de l'arrière plan et du bouton buttonStart
    mainScreen.blit(background, (0,0))
    mainScreen.blit(buttonStart.image,buttonStart.rect)
    pygame.display.flip()

    # Condition d'évènements
    for event in pygame.event.get():

        # Fermeture du jeu lors d'un clique sur la croix
        if event.type == QUIT:
            running = False
            pygame.quit()

        # lors d'un clique sur le bouton start
        if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.rect.collidepoint(event.pos):
                    print("Le bouton a été cliqué !")



"""
class Jeu:
    
    def __init__(self):
        self.etat = "Accueil" # Les différents états possibles sont: "Accueil", "Trone", "Quete1" et "Quete 2"


class guerrier:

    def __init__(self):
        self.health = 1
        self.max_health = 1
        # à suivre
"""