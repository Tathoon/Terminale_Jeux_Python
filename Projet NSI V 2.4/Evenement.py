import pygame

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

    def transition_Menu_accueil_ChoixBase(self, event, menu_accueil, choixBase):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_accueil.buttonStart.rect.collidepoint(event.pos):
                menu_accueil.is_active = False
                choixBase.is_active = True
        return menu_accueil.is_active,choixBase.is_active