# Importation de Pygame et chargement de ses composants
import pygame
from pygame.locals import *
from pygame import mixer
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

# Initialisation des musiques
mixer.music.load("musicecranaccueil.mp3")
mixer.music.play(-1)

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
            menu_accueil.is_active, choixBase.is_active = evenement.transition_Menu_accueil_ChoixBase(event, menu_accueil, choixBase)

    elif choixBase.is_active == True:
        choixBase.update(mainScreen, choixBase.background)
        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            choixBase.is_active, accueil.is_active, pnj.is_active = evenement.transition_ChoixBase_Accueil(event, choixBase, accueil, pnj)

    elif accueil.is_active == True and pnj.is_active == True:
        accueil.update(mainScreen, menu_accueil.background)
        pnj.update(mainScreen)


        evenement.mouvement_joueur(pnj, mainScreen)
        if pnj.type.pos.x < -15:
            """
            accueil.is_active = False
            pnj.is_active = False
            menu_quetes.is_active = True
            """


        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)

    elif menu_quetes.is_active == True:
        menu_quetes.update(mainScreen,menu_quetes.background)
        mainScreen.blit(buttonRetour.image,buttonRetour.rect)
        for event in pygame.event.get():
            running = evenement.gerer_quitter(event, running)
            menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event,  buttonRetour, menu_quetes, menu_accueil)

    pygame.display.flip()

    # Permet le contrôle des fps du jeu
    clock = pygame.time.Clock()
    clock.tick(160)