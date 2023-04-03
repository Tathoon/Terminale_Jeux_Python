import pygame
from Game import game, guerrier, mage

class evenement:
    """ Pour cette classe de gestion d'évènement qui n'ont pas de caractéristiques,
    on n'utilise pas de constructeurs"""
    def __init__(self):
        pygame.init()

    def gerer_quitter(self, event, running):
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        return running

    def retour_to_menu_accueil(self, event, buttonRetour, menu_quetes, menu_accueil):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonRetour.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                menu_accueil.is_active = True
        return menu_quetes.is_active, menu_accueil.is_active

    def mouvement_joueur(self, pnj, mainScreen):
        if pnj.pressed.get(pygame.K_RIGHT) and pnj.type.pos.x + pnj.type.pos.width < mainScreen.get_width():
            pnj.move_right()
        elif pnj.pressed.get(pygame.K_LEFT):
            pnj.move_left()

    def touches_pressees(self, event, pnj):
        if event.type == pygame.KEYDOWN:
            pnj.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pnj.pressed[event.key] = False
        return pnj.pressed[event.key]

    def transition_Menu_accueil_ChoixBase(self, event, menu_accueil, choixBase):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_accueil.buttonStart.rect.collidepoint(event.pos):
                menu_accueil.is_active = False
                choixBase.is_active = True
        return menu_accueil.is_active, choixBase.is_active

    def transition_ChoixBase_Accueil(self, event, choixBase, accueil, pnj):
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
        return choixBase.is_active, accueil.is_active, pnj.is_active