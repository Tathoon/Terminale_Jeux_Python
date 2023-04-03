# Importation de Pygame et chargement de ses composants
import pygame
from pygame.locals import *
pygame.init()

# Importation des classes depuis leur fichier d'enregistrement
from Button import button
from Menu import menu_accueil, menu_quetes
from Accueil import accueil
from Choix import choixBase
from Game import game, guerrier, mage
from Evenement import evenement

# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

# Création des objets de classes
menu_accueil = menu_accueil(mainScreen)
accueil = accueil(mainScreen)
choixBase = choixBase(mainScreen)
menu_quetes = menu_quetes(mainScreen)
pnj = game()
evenement = evenement()

running = True

buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70) # Un bouton de retour présent uniquement sur certaines pages
listePages = [choixBase, accueil, menu_quetes] #La listes des pages sans le menu d'accueil

# Boucle du jeu
while running:
    if menu_accueil.is_active == True:
        menu_accueil.update(mainScreen, menu_accueil.background)
        # lors d'un clique sur le bouton start
        for event in pygame.event.get():
            running = evenement.gerer_quitter(event,running)
            menu_accueil.is_active,choixBase.is_active = evenement.transition_Menu_accueil_ChoixBase(event,menu_accueil,choixBase)

    elif choixBase.is_active == True:
        choixBase.update(mainScreen, choixBase.background)
        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                if choixBase.buttonChoixA.rect.collidepoint(event.pos):
                    choixBase.is_active = False
                    accueil.is_active = True
                    pnj.is_active = True
                    pnj.type = guerrier()
                    pnj.depart_accueil()
                elif choixBase.buttonChoixB.rect.collidepoint(event.pos):
                    choixBase.is_active = False
                    pnj.is_active = True
                    accueil.is_active = True
                    pnj.type = mage()
                    pnj.depart_accueil()
            """

    elif accueil.is_active == True and pnj.is_active == True:
        accueil.update(mainScreen, menu_accueil.background)
        pnj.update(mainScreen)
        """
        if pnj.pressed.get(pygame.K_RIGHT) and pnj.type.pos.x + pnj.type.pos.width < mainScreen.get_width(): #Tant que le pnj ne sort pas de l'écran par la droite
            pnj.move_right()     
        elif pnj.pressed.get(pygame.K_LEFT): #dans ce cas ci le pnj peut aller à gauche sans être limité car switch sur une page quetes
            pnj.move_left()
        if pnj.type.pos.x < -15:
            accueil.is_active = False
            pnj.is_active = False
            menu_quetes.is_active = True
        """

        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            """
            if event.type == pygame.KEYDOWN:
                pnj.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                pnj.pressed[event.key] = False
            """

    elif menu_quetes.is_active == True:
        menu_quetes.update(mainScreen,menu_quetes.background)
        mainScreen.blit(buttonRetour.image,buttonRetour.rect)
        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonRetour.rect.collidepoint(event.pos):
                    menu_quetes.is_active = False
                    menu_accueil.is_active = True
            """
    
    pygame.display.flip()         
    
    # Permet le contrôle des fps du jeu
    clock = pygame.time.Clock()
    clock.tick(160)
