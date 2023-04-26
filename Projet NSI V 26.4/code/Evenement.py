import pygame
from Game import game, guerrier, mage
from Projectile import projectile
from Pile import pile

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

    def __init__(self, menu_accueil, mainScreen):
        pygame.init()
        self.pile_retour = pile()
        self.pile_retour.empiler(menu_accueil)
        self.mainScreen = mainScreen

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

    """def retour_to_menu_accueil(self, event, menu_quetes, menu_accueil):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_quetes.buttonRetour.rect.collidepoint(event.pos):
                menu_quetes.is_active = False
                menu_accueil.is_active = True"""
                
    def retour(self, event, page, page_suiv_nom, pnj, soundDesign):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if page.buttonRetour.rect.collidepoint(event.pos):
                self.pile_retour.depiler().is_active = False
                self.musiques_retour(page_suiv_nom, soundDesign)
                self.pile_retour.depiler().is_active = True
                if pnj != None:
                    pnj.depart_accueil(self.mainScreen)

    def touches_pressees(self, event, pnj):
        if event.type == pygame.KEYDOWN:
            pnj.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pnj.pressed[event.key] = False



    def run_menu_accueil(self, running, event, menu_accueil, choixBase, soundDesign):
        self.gerer_quitter(event, running)
        self.transit_page(event, menu_accueil.buttonStart, menu_accueil, "menu_accueil", choixBase, "choixBase", None, soundDesign)

    def run_choixBase(self, running, event, choixBase, accueil, pnj, mainScreen, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, choixBase, "menu_accueil", None, soundDesign)
        self.transit_page(event, choixBase.buttonChoixA, choixBase, "choixBase.buttonChoixA", accueil, "accueil", pnj, soundDesign)
        self.transit_page(event, choixBase.buttonChoixB, choixBase, "choixBase.buttonChoixB", accueil, "accueil", pnj, soundDesign)
    
    def run_accueil(self, running, event, pnj, accueil, menu_quetes, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, accueil, "choixBase", None, soundDesign)
        self.transit_page(None, None, accueil, "accueil", menu_quetes, "menu_quetes", pnj, soundDesign)
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.touches_pressees(event, pnj)
    
    def run_menu_quetes(self, running, event, pnj, menu_quetes, menu_accueil, descri_quete1, descri_quete2, descri_quete3, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, menu_quetes, "accueil", pnj, soundDesign)
        self.transit_page(event, menu_quetes.button_Quete1, menu_quetes, "menu_quetes", descri_quete1, "descri_quete1", None, soundDesign)
        self.transit_page(event, menu_quetes.button_Quete2, menu_quetes, "menu_quetes", descri_quete2, "descri_quete2", None, soundDesign)
        self.transit_page(event, menu_quetes.button_Quete3, menu_quetes, "menu_quetes", descri_quete3, "descri_quete3", None, soundDesign)

    def run_descri_quete1(self, running, event, menu_quetes, menu_accueil, descri_quete1, quete1, pnj, mainScreen, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, descri_quete1, "menu_quetes", None, soundDesign)
        self.transit_page(event, descri_quete1.lancer, descri_quete1, "descri_quete1", quete1, "quete1", pnj, soundDesign)

    def run_descri_quete2(self, running, event, menu_quetes, menu_accueil, descri_quete2, quete2, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, descri_quete2, "menu_quetes", None, soundDesign)
        self.transit_page(event, descri_quete2.lancer, descri_quete2, "descri_quete2", quete2, "quete2", None, soundDesign)

    def run_descri_quete3(self, running, event, menu_quetes, menu_accueil, descri_quete3, quete3, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, descri_quete3, "menu_quetes", None, soundDesign)
        self.transit_page(event, descri_quete3.lancer, descri_quete3, "descri_quete3", quete3, "quete3", None, soundDesign)

    def run_quete1(self, running, event, quete1, pnj, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, quete1, "descri_quete1", None, soundDesign)
        if event.type == pygame.KEYDOWN:
            # Lancement des évènement de déplacements.
            self.touches_pressees(event, pnj)
            self.tirer(event, pnj)
        elif event.type == pygame.KEYUP:
            self.touches_pressees(event, pnj)

    def run_quete2(self, running, event, quete2, soundDesign):
        self.gerer_quitter(event, running)
        self.retour(event, quete2, "descri_quete2", None, soundDesign)

    def run_defaite(self, running, event, defaite, menu_quetes, soundDesign):
        self.gerer_quitter(event, running)
        self.transit_page(event, defaite.retour_menu_quete, defaite, "defaite", menu_quetes, "menu_quetes", None, soundDesign)



    def transit_page(self, event, bouton, page_actu, page_actu_nom, page_suiv, page_suiv_nom, pnj, soundDesign):
        if page_actu_nom == "accueil":
            if pnj.type.rect.x < -15:
                page_actu.is_active = False
                page_suiv.is_active = True
                page_suiv.partie = 1

                pygame.mixer.music.stop()
                soundDesign.play_music("menu_quetes", 1)
                self.pile_retour.empiler(page_actu)
                self.pile_retour.empiler(page_suiv)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if page_actu_nom == "menu_accueil":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "choixBase.buttonChoixA":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True
                    pnj.type = guerrier()
                    pnj.all_player.add(pnj.type)
                    pnj.depart_accueil(self.mainScreen)

                    page_suiv.update_arrive(self.mainScreen, page_actu, pnj, self) # Fondu
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "choixBase.buttonChoixB":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True
                    pnj.type = mage()
                    pnj.all_player.add(pnj.type)
                    pnj.depart_accueil(self.mainScreen)
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "menu_quetes":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "descri_quete1":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True
                    pnj.depart_accueil(self.mainScreen)
                    page_suiv.update_arrive(pnj, self.mainScreen)

                    pygame.mixer.music.stop()
                    soundDesign.play_music("quete1", 1)
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "descri_quete2":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True

                    pygame.mixer.music.stop()
                    soundDesign.play_music("quete2", 1)
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)

            elif page_actu_nom == "descri_quete3":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True

                    pygame.mixer.music.stop()
                    soundDesign.play_music("quete3", 1)
                    self.pile_retour.empiler(page_actu)
                    self.pile_retour.empiler(page_suiv)
            
            elif page_actu_nom == "defaite":
                if bouton.rect.collidepoint(event.pos):
                    page_actu.is_active = False
                    page_suiv.is_active = True

                    pygame.mixer.music.stop()
                    soundDesign.play_music("menu_quetes", 1)
                    self.pile_retour.depiler()
                    self.pile_retour.depiler()

    def transit_Quete1_Defaite(self, quete1, defaite):
        quete1.is_active = False
        defaite.is_active = True

    def musiques_retour(self, page_actu_nom, soundDesign): #Lors de l'utilisation du bouton retour, il faut bien dsistinguer les groupes de pages pour chaque musiques
        if page_actu_nom == "descri_quete1" or page_actu_nom == "descri_quete2" or page_actu_nom == "descri_quete3":
            pygame.mixer.music.stop()
            soundDesign.play_music("menu_quetes", 1)
        elif page_actu_nom == "accueil":
            pygame.mixer.music.stop()
            soundDesign.play_music("intro", 1)