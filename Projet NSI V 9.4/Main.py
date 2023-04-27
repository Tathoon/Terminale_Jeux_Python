# Importation de Pygame et chargement de ses composants
import pygame
from pygame import *
pygame.init()

# Importation des classes depuis leur fichier d'enregistrement
from Pages import *
from Game import game, guerrier, mage
from Evenement import evenement

# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

# Initialisation des musiques
mixer.music.load("musiques/musicecranaccueil.mp3") # Import avec le chemin
mixer.music.set_volume(0) # Gestion du volume
mixer.music.play(-1) # Mis en route de la musique. La valeur -1 permet de la jouer en continu

# Création des objets de classes
menu_accueil = menu_accueil(mainScreen) # La classe menu_accueil (première page) permet la gestion des objets de cette classe
choixBase = choixBase(mainScreen) # La classe choixBase (page de choix de personnage) permet la gestion des objets de cette classe
accueil = accueil(mainScreen) # La classe accueil (salle du roi précédant les quetes) permet la gestion des objets de cette classe
menu_quetes = menu_quetes(mainScreen) # La classe menu_quetes (page de choix de quetes) permet la gestion des objets de cette classe
pnj = game() # La classe game permet de gérer les déplacement de personnages
evenement = evenement() # La classe evenement permet la gestion de tout les évènements du jeu
quete1 = quete1(mainScreen)
quete2 = quete2(mainScreen)
quete3 = quete3(mainScreen)

listePages = [choixBase, accueil, menu_quetes] #La listes des pages sans le menu d'accueil
running = True
# Boucle du jeu
while running:
    if menu_accueil.is_active == True:
        menu_accueil.update(mainScreen) # On applique les éléments relatif à la page menu_accueil
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "changements de page (de Menu Accueil à ChoixBase)"
            running = evenement.gerer_quitter(event,running)
            menu_accueil.is_active, choixBase.is_active = evenement.transition_Menu_accueil_ChoixBase(event, menu_accueil, choixBase)

    elif choixBase.is_active == True:
        choixBase.update(mainScreen) # On applique les éléments relatif à la page choixBase
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "changements de page (de ChoixBase à Accueil)"
            running = evenement.gerer_quitter(event, running)
            choixBase.is_active, accueil.is_active, pnj.is_active = evenement.transition_ChoixBase_Accueil(event, choixBase, accueil, pnj, mainScreen)

    elif accueil.is_active == True and pnj.is_active == True:
        accueil.update(mainScreen, pnj, evenement) # On applique les éléments relatif à la page accueil
        # Lancement des évènement "changements de page (de Accueil à Menu_Quetes) lorsque le personnage sort par la gauche"
        accueil.is_active, pnj.is_active, menu_quetes.is_active, menu_quetes.partie = evenement.transition_Accueil_Menu_Quetes(event, accueil, pnj, menu_quetes)
        for event in pygame.event.get():
            # Lancement de l'évènement "quitter"
            running = evenement.gerer_quitter(event, running)
            # Lors du clique sur une touche ou du relachement d'une touche
            if event.type == pygame.KEYDOWN:
                # Lancement des évènement de déplacements.
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)
            elif event.type == pygame.KEYUP:
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)

    elif menu_quetes.is_active == True:
        if menu_quetes.partie == 1:
            menu_quetes.update_partie1(mainScreen) # On applique les éléments relatif à la page menu_quetes
            for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "retour au menu"
                running = evenement.gerer_quitter(event, running)
                menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
                menu_quetes.partie, menu_quetes.descri_Quete = evenement.transition_descri_Quetes(event, menu_quetes)
       
        elif menu_quetes.partie == 2:
            if menu_quetes.descri_Quete == 1:
                menu_quetes.update_quete1(mainScreen)
                for event in pygame.event.get():
                # Lancement des évènement. Ici : "quitter" et "retour au menu"
                    running = evenement.gerer_quitter(event, running)
                    menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
                    menu_quetes.is_active, menu_quetes.partie, quete1.is_active, pnj.is_active = evenement.transition_Quete1(event, menu_quetes, quete1, pnj, mainScreen)

            elif menu_quetes.descri_Quete == 2:
                menu_quetes.update_quete2(mainScreen)
                for event in pygame.event.get():
                # Lancement des évènement. Ici : "quitter" et "retour au menu"
                    running = evenement.gerer_quitter(event, running)
                    menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
                    menu_quetes.is_active, menu_quetes.partie, quete2.is_active = evenement.transition_Quete2(event, menu_quetes, quete2)

            elif menu_quetes.descri_Quete == 3:
                menu_quetes.update_quete3(mainScreen)
                for event in pygame.event.get():
                # Lancement des évènement. Ici : "quitter" et "retour au menu"
                    running = evenement.gerer_quitter(event, running)
                    menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
                    menu_quetes.is_active, menu_quetes.partie, quete3.is_active = evenement.transition_Quete3(event, menu_quetes, quete3)

    elif quete1.is_active == True and pnj.is_active == True:
        quete1.update(mainScreen, pnj, evenement)
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "retour au menu"
            running = evenement.gerer_quitter(event, running)
            if event.type == pygame.KEYDOWN:
                # Lancement des évènement de déplacements.
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)
                evenement.tirer(event, pnj)
            elif event.type == pygame.KEYUP:
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)

    elif quete2.is_active == True:
        quete2.update(mainScreen)
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "retour au menu"
            running = evenement.gerer_quitter(event, running)

    elif quete3.is_active == True:
        quete3.update(mainScreen)
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "retour au menu"
            running = evenement.gerer_quitter(event, running)

    pygame.display.flip() # actualise la page

    # Permet le contrôle des fps du jeu
    clock = pygame.time.Clock()
    clock.tick(160)