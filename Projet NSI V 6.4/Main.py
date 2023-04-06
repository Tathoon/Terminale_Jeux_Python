# Importation de Pygame et chargement de ses composants
import pygame
from pygame import *
pygame.init()

# Importation des classes depuis leur fichier d'enregistrement
from Pages import accueil, choixBase, menu_accueil, menu_quetes
from Game import game, guerrier, mage
from Evenement import evenement

# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

# Initialisation des musiques
mixer.music.load("musiques/musicecranaccueil.mp3") # Import avec le chemin
mixer.music.set_volume(0.4) # Gestion du volume
mixer.music.play(-1) # Mis en route de la musique. La valeur -1 permet de la jouer en continu

# Création des objets de classes
menu_accueil = menu_accueil(mainScreen) # La classe menu_accueil (première page) permet la gestion des objets de cette classe
choixBase = choixBase(mainScreen) # La classe choixBase (page de choix de personnage) permet la gestion des objets de cette classe
accueil = accueil(mainScreen) # La classe accueil (salle du roi précédant les quetes) permet la gestion des objets de cette classe
menu_quetes = menu_quetes(mainScreen) # La classe menu_quetes (page de choix de quetes) permet la gestion des objets de cette classe
pnj = game() # La classe game permet de gérer les déplacement de personnages
evenement = evenement() # La classe evenement permet la gestion de tout les évènements du jeu

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
            choixBase.is_active, accueil.is_active, pnj.is_active = evenement.transition_ChoixBase_Accueil(event, choixBase, accueil, pnj)

    elif accueil.is_active == True and pnj.is_active == True:
        accueil.update(mainScreen, pnj, evenement) # On applique les éléments relatif à la page accueil
        if pnj.type.pos.x < -15:
            # Lancement des évènement "changements de page (de Accueil à Menu_Quetes) lorsque le personnage sort par la gauche"
            accueil.is_active, pnj.is_active, menu_quetes.is_active = evenement.transition_Accueil_Menu_Quetes(event, accueil, pnj, menu_quetes)
        for event in pygame.event.get():
            # Lancement de l'évènement "quitter"
            running = evenement.gerer_quitter(event, running)
            # Lors du clique sur une touche ou du relachement d'une touche
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                # Lancement des évènement de déplacements.
                pnj.pressed[event.key] = evenement.touches_pressees(event, pnj)

    elif menu_quetes.is_active == True:
        menu_quetes.update(mainScreen) # On applique les éléments relatif à la page manu_quetes
        for event in pygame.event.get():
            # Lancement des évènement. Ici : "quitter" et "retour au menu"
            running = evenement.gerer_quitter(event, running)
            menu_quetes.is_active, menu_accueil.is_active = evenement.retour_to_menu_accueil(event, menu_quetes, menu_accueil)

    pygame.display.flip() # actualise la page

    # Permet le contrôle des fps du jeu
    clock = pygame.time.Clock()
    clock.tick(160)