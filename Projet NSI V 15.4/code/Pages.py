import pygame
from Button import button, descriptions #renommer Button par elements
from Projectile import projectile
from Fondu import *

class menu_accueil:
    """
    Classe qui permet la gestion des éléments de la page menu_accueil

    ### attributs:
        - is_active : Booléen qui indique si la page est active
        - background : Fond d'écran de la page
        - buttonStart : Un bouton (il est utilisé pour lancer le jeu)

    ### méthodes:
        - update -> Applique les éléments background et buttonStart
    """

    def __init__(self, mainScreen):
        self.is_active = True
        # Importation de l'arrière plan
        self.background = pygame.transform.scale(pygame.image.load('assets/background/mainBack01.jpg'),(mainScreen.get_size()))
        #Création d'un bouton Start
        self.buttonStart = button("assets/button/startbutton02.png", 305, 135, 395, 460)

    def update(self, mainScreen, soundDesign):
        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonStart.image,self.buttonStart.rect)
        if not soundDesign.menu_accueil_is_active:
            soundDesign.play_music("menu_accueil", 0.01)
            soundDesign.menu_accueil_is_active = True

class choixBase:
    """
    Classe qui permet la gestion des éléments de la page choixBase

    ### attributs:
        - is_active : Booléen qui indique si la page est active
        - background : Fond d'écran de la page
        - buttonChoixA : Un bouton (il est utiliser pour passer à la page accueil avec le choix d'un personnnage type guerrier)
        - buttonChoixB : Un second bouton (il est utiliser pour passer à la page accueil avec le choix d'un personnnage type guerrier)

    ### méthodes:
        - update -> Applique les éléments background, buttonChoixA et buttonChoixB
    """

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/mainBack01.jpg'),(mainScreen.get_size()))
        self.buttonChoixA = button("assets/choice/choixA.jpg", 200, 400, 450, mainScreen.get_height()-400)
        self.buttonChoixB = button("assets/choice/choixB.jpg", 200, 400, mainScreen.get_width()-450, mainScreen.get_height()-400)
        
    def update(self, mainScreen):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonChoixA.image,self.buttonChoixA.rect)
        mainScreen.blit(self.buttonChoixB.image,self.buttonChoixB.rect)

class accueil:
    """
    Classe qui permet la gestion des éléments de la page accueil

    ### attributs:
        - is_active : Booléen qui indique si la page est active
        - background : Fond d'écran de la page

    ### méthodes:
        - update -> Applique les éléments background, appel la méthode update de la classe game et appel la méthode mouvement_joueur de la classe evenement
    """

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuBack01.jpg'),(mainScreen.get_size()))
    
    def update_arrive(self, mainScreen, choixBase, pnj, evenement):
        change_image_with_transition(choixBase.background, self.background, (0,0,255), 3, mainScreen)
        pnj.update(mainScreen)
        evenement.mouvement_joueur(pnj, mainScreen)

    def update(self, mainScreen, pnj, evenement):
        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        pnj.update(mainScreen)
        evenement.mouvement_joueur(pnj, mainScreen)

class menu_quetes:
    """
    Classe qui permet la gestion des éléments de la page menu_quetes

    ### attributs:
        - is_active : Booléen qui indique si la page est active
        - background : Fond d'écran de la page
        - buttonRetour : Un bouton (il est utilisé pour retourner à la page menu_accueil)

    ### méthodes:
        - update -> Applique les éléments background et buttonRetour
    """

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuQuetes.jpg'),(mainScreen.get_size()))
        self.buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70)
        self.button_Quete1 = button('assets/button/button_quete1.png', 250, 125, mainScreen.get_width()/2, 200)
        self.button_Quete2 = button('assets/button/button_quete2.png', 250, 125, mainScreen.get_width()/2, 350)
        self.button_Quete3 = button('assets/button/button_quete3.png', 250, 125, mainScreen.get_width()/2, 500)

    def update(self, mainScreen):
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonRetour.image, self.buttonRetour.rect)
        mainScreen.blit(self.button_Quete1.image, self.button_Quete1.rect)
        mainScreen.blit(self.button_Quete2.image, self.button_Quete2.rect)
        mainScreen.blit(self.button_Quete3.image, self.button_Quete3.rect)

class descri_quete1:

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuQuetes.jpg'),(mainScreen.get_size()))
        self.buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70)
        self.descri = descriptions('assets/descriptions quetes/Descri_Quete1.png', 600, 320, mainScreen.get_width()/2, 250)
        self.lancer = button('assets/button/lancer.png', 400, 100, mainScreen.get_width()/2, 470)

    def update(self, mainScreen):
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonRetour.image, self.buttonRetour.rect)
        mainScreen.blit(self.descri.image, self.descri.rect)
        mainScreen.blit(self.lancer.image, self.lancer.rect)

class descri_quete2:

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuQuetes.jpg'),(mainScreen.get_size()))
        self.buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70)
        self.descri = descriptions('assets/descriptions quetes/Descri_Quete2.png', 600, 320, mainScreen.get_width()/2, 250)
        self.lancer = button('assets/button/lancer.png', 400, 100, mainScreen.get_width()/2, 470)

    def update(self, mainScreen):
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonRetour.image, self.buttonRetour.rect)
        mainScreen.blit(self.descri.image, self.descri.rect)
        mainScreen.blit(self.lancer.image, self.lancer.rect)

class descri_quete3:

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuQuetes.jpg'),(mainScreen.get_size()))
        self.buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70)
        self.descri = descriptions('assets/descriptions quetes/Descri_Quete3.png', 600, 320, mainScreen.get_width()/2, 250)
        self.lancer = button('assets/button/lancer.png', 400, 100, mainScreen.get_width()/2, 470)

    def update(self, mainScreen):
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonRetour.image, self.buttonRetour.rect)
        mainScreen.blit(self.descri.image, self.descri.rect)
        mainScreen.blit(self.lancer.image, self.lancer.rect)

class quete1:

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/quete1_Back.jpg'),(mainScreen.get_size()))

    def update_arrive(self, pnj, mainScreen):
        pnj.spawn_monster(mainScreen)

    def update(self, mainScreen, pnj, evenement, defaite, soundDesign):
        # ajour de l'arrière plan et du bouton buttonStart
        if not soundDesign.quete1_is_active:
            pygame.mixer.music.stop()
            soundDesign.play_music("quete1", 0.1)
            soundDesign.quete1_is_active = True
        mainScreen.blit(self.background, (0,0))
        pnj.update(mainScreen)
        pnj.update_health_bar(mainScreen)
        evenement.mouvement_joueur(pnj, mainScreen)
        for projectile in pnj.all_projectiles:
            projectile.move(mainScreen, pnj)
        pnj.all_projectiles.draw(mainScreen)
        for monster in pnj.all_monster:
            pnj.monster_vers_joueurs(monster, pnj, evenement, self, defaite)
            monster.update_health_bar(mainScreen)
        pnj.all_monster.draw(mainScreen)
        

class quete2:

    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/quete2_Back.png'),(mainScreen.get_size()))

    def update(self, mainScreen):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))

class quete3:

    def __init__(self, mainScreen):
        self.is_active = False
        
class defaite:
    
    def __init__(self, mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/back_mort.png'),(mainScreen.get_size()))

    def update(self, mainScreen):
        # ajout de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))