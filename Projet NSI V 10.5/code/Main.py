# Importation de Pygame et chargement de ses composants
import pygame
from pygame import *
pygame.init()

# Importation des classes depuis leur fichier d'enregistrement
from Pages import *
from Game import *
from Game_reve import monde_reve
from Evenement import *
from Musique import soundDesign

# Création de la fenêtre
mainScreen = pygame.display.set_caption("Une ère paisible") # Nommage de la fenêtre
mainScreen = pygame.display.set_icon(pygame.image.load("assets/monster/mario.png")) # Définition d'une icone de fenêtre
mainScreen = pygame.display.set_mode((1280, 720)) # Création et définition des dimmensions de la fenêtre

# Création des objets de classes pour chaque pages
menu_accueil = menu_accueil(mainScreen)
choixBase = choixBase(mainScreen)
accueil = accueil(mainScreen)
menu_quetes = menu_quetes(mainScreen)
descri_quete1 = descri_quete1(mainScreen)
descri_quete2 = descri_quete2(mainScreen)
descri_quete3 = descri_quete3(mainScreen)
quete1 = quete1(mainScreen)
quete2 = quete2(mainScreen)
quete3 = quete3(mainScreen)
monde_reve = monde_reve(mainScreen)
defaite = defaite(mainScreen)

soundDesign = soundDesign() # Classe de gestion des sons
soundDesign.play_music("intro", 1, -1)

evenement = evenement(menu_accueil, mainScreen) # Classe de gestion des évènements
pnj = game() # Classe de gestion du jeu

running = True
# Boucle du jeu
while running:

    if menu_accueil.is_active:
        menu_accueil.update(mainScreen, soundDesign) # On applique les éléments relatif à la page menu_accueil
        for event in pygame.event.get():
            evenement.run_menu_accueil(running, event, menu_accueil, choixBase, soundDesign)

    elif choixBase.is_active:
        choixBase.update(mainScreen) # On applique les éléments relatif à la page choixBase
        for event in pygame.event.get():
            evenement.run_choixBase(running, event, choixBase, accueil, pnj, mainScreen, soundDesign)

    elif accueil.is_active:
        accueil.update(mainScreen, pnj, evenement) # On applique les éléments relatif à la page accueil
        for event in pygame.event.get():
            evenement.run_accueil(running, event, pnj, accueil, menu_quetes, soundDesign)

    elif menu_quetes.is_active:
        menu_quetes.update(mainScreen) # On applique les éléments relatif à la page menu_quetes
        for event in pygame.event.get():
            evenement.run_menu_quetes(running, event, pnj, menu_quetes, menu_accueil, descri_quete1, descri_quete2, descri_quete3, soundDesign)
       
    elif descri_quete1.is_active:
        descri_quete1.update(mainScreen)
        for event in pygame.event.get():
            evenement.run_descri_quete1(running, event, menu_quetes, menu_accueil, descri_quete1, quete1, pnj, mainScreen, soundDesign)

    elif descri_quete2.is_active:
        descri_quete2.update(mainScreen)
        for event in pygame.event.get():
            evenement.run_descri_quete2(running, event, menu_quetes, menu_accueil, descri_quete2, quete2, soundDesign)

    elif descri_quete3.is_active:
        descri_quete3.update(mainScreen)
        for event in pygame.event.get():
            evenement.run_descri_quete3(running, event, menu_quetes, menu_accueil, descri_quete3, quete3, soundDesign)

    elif quete1.is_active:
        quete1.update(mainScreen, pnj, evenement, defaite, soundDesign)
        for event in pygame.event.get():
            evenement.run_quete1(running, event, quete1, pnj, soundDesign)

    elif quete2.is_active:
        quete2.update(mainScreen)
        for event in pygame.event.get():
            evenement.run_quete2(running, event, quete2, soundDesign)

    elif quete3.is_active:
        monde_reve.run()

    elif defaite.is_active:
        defaite.update(mainScreen)
        for event in pygame.event.get():
            evenement.run_defaite(running, event, defaite, menu_quetes, soundDesign)

    pygame.display.flip() # actualise la page

    # Permet le contrôle des fps du jeu
    clock = pygame.time.Clock()
    clock.tick(160)