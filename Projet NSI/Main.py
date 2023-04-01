# Importation de Pygame et chargement de ses composants
import pygame
from pygame.locals import *
pygame.init()

# Importation des classes depuis leur fichier d'enregistrement
from Button import button
from Menu import menu
from Accueil import accueil
from Choix import choixBase

# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

menu = menu(mainScreen)
accueil = accueil(mainScreen)
choixBase = choixBase(mainScreen)
running = True
# Boucle du jeu

while running:
    
    if menu.is_active == True:
        menu.update(mainScreen, menu.background)
        # lors d'un clique sur le bouton start
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.buttonStart.rect.collidepoint(event.pos):
                    print("Le bouton a été cliqué !")
                    menu.is_active = False
                    choixBase.is_active = True

    elif choixBase.is_active == True:
        choixBase.update(mainScreen, choixBase.background)

    elif accueil.is_active == True:
        accueil.update(mainScreen, menu.background)

    pygame.display.flip()

    # Condition d'évènements
    for event in pygame.event.get():
        # Fermeture du jeu lors d'un clique sur la croix
        if event.type == QUIT:
            running = False
            pygame.quit()





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