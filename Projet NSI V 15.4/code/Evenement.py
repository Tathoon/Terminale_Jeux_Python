import pygame
from Game import game, guerrier, mage
from Projectile import projectile

class evenement:
    """
    Classe qui permet la gestion de l'ensemble des évènements générés par l'utilisateur

    ### attributs:
        - Pas d'attributs --> la classe ne sert qu'à regrouper un grand nombre de méthodes pratiques en lien avec les différents évènements

    ### méthodes:
        - gerer_quitter -> ferme la fenêtre lorsque l'utilisateur appuie sur la croix
        - mouvement_joueur -> détecte les touches du clavier enfoncées et fait appel à la méthode de déplacement du joueur correspondante de la classe Game
        - retour_to__menu_accueil -> gère l'évènement retour au menu engendré par l'appui sur le bouton correspondant de la classe Button
        - touches_presses -> détecte si l'utilisateur appuie sur une touche du clavier et/ou si à l'inverse il lache une touche
        - transition_Menu_accueil_ChoixBase -> gère la transition entre le menu et le choix de la classe du personnage
        - transition_ChoixBase_Accueil -> gère la transition entre le choix de la classe du personnage et la page d'accueil
        - transition_Accueil_Menu_Quetes -> gère la transition etre la page d'accueil et le menu des quetes
    """

    def __init__(self):
        pygame.init()

    def gerer_quitter(self, event, running):
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    def mouvement_joueur(self, pnj, mainScreen):
        if pnj.pressed.get(pygame.K_d) and pnj.type.rect.x + pnj.type.rect.width < mainScreen.get_width():
            pnj.move_right()
        elif pnj.pressed.get(pygame.K_q):
            pnj.move_left()

    def tirer(self, event, pnj):
        if event.key == pygame.K_SPACE:
            pnj.tirer(pnj)

    def retour_to_menu_accueil(self, event, menu_quetes, menu_accueil):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_quetes.buttonRetour.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                menu_accueil.is_active = True

    def touches_pressees(self, event, pnj):
        if event.type == pygame.KEYDOWN:
            pnj.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pnj.pressed[event.key] = False

    def transition_Quete1_Defaite(self, quete1, defaite):
        quete1.is_active = False
        defaite.is_active = True






    def run_menu_accueil(self, running, event, menu_accueil, choixBase):
        self.gerer_quitter(event, running)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_accueil.buttonStart.rect.collidepoint(event.pos):
                menu_accueil.is_active = False
                choixBase.is_active = True

    def run_choixBase(self, running, event, choixBase, accueil, pnj, mainScreen):
        self.gerer_quitter(event, running)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if choixBase.buttonChoixA.rect.collidepoint(event.pos):
                choixBase.is_active = False
                accueil.is_active = True
                pnj.type = guerrier()
                pnj.all_player.add(pnj.type)
                pnj.depart_accueil(mainScreen)
                accueil.update_arrive(mainScreen, choixBase, pnj, self)
            elif choixBase.buttonChoixB.rect.collidepoint(event.pos):
                choixBase.is_active = False
                accueil.is_active = True
                pnj.type = mage()
                pnj.all_player.add(pnj.type)
                pnj.depart_accueil(mainScreen)
    
    def run_accueil(self, running, event, accueil, pnj, menu_quetes):
        self.gerer_quitter(event, running)
        if pnj.type.rect.x < -15:
            accueil.is_active = False
            menu_quetes.is_active = True
            menu_quetes.partie = 1
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.touches_pressees(event, pnj)
    
    def run_menu_quetes(self, running, event, menu_quetes, menu_accueil, descri_quete1, descri_quete2, descri_quete3):
        self.gerer_quitter(event, running)
        # self.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_quetes.button_Quete1.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                descri_quete1.is_active = True
            elif menu_quetes.button_Quete2.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                descri_quete2.is_active = True
            elif menu_quetes.button_Quete3.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                descri_quete3.is_active = True

    def run_descri_quete1(self, running, event, menu_quetes, menu_accueil, descri_quete1, quete1, pnj, mainScreen, soundDesign):
        self.gerer_quitter(event, running)
        # self.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if descri_quete1.lancer.rect.collidepoint(event.pos):
                soundDesign.menu_accueil_is_active = False
                descri_quete1.is_active = False
                quete1.is_active = True
                pnj.depart_accueil(mainScreen)
                quete1.update_arrive(pnj, mainScreen)

    def run_descri_quete2(self, running, event, menu_quetes, menu_accueil, descri_quete2, quete2):
        self.gerer_quitter(event, running)
        self.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if descri_quete2.lancer.rect.collidepoint(event.pos):
                descri_quete2.is_active = False
                quete2.is_active = True

    def run_descri_quete3(self, running, event, menu_quetes, menu_accueil, descri_quete3, quete3):
        self.gerer_quitter(event, running)
        self.retour_to_menu_accueil(event, menu_quetes, menu_accueil)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if descri_quete3.lancer.rect.collidepoint(event.pos):
                descri_quete3.is_active = False
                quete3.is_active = True

    def run_quete1(self, running, event, pnj):
        self.gerer_quitter(event, running)
        if event.type == pygame.KEYDOWN:
            # Lancement des évènement de déplacements.
            self.touches_pressees(event, pnj)
            self.tirer(event, pnj)
        elif event.type == pygame.KEYUP:
            self.touches_pressees(event, pnj)