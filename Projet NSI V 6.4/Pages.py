import pygame
from Button import button

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

    def update(self, mainScreen):

        # ajour de l'arrière plan et du bouton buttonStart
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonStart.image,self.buttonStart.rect)

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

    def __init__(self,mainScreen):
        self.is_active = False
        self.background = pygame.transform.scale(pygame.image.load('assets/background/menuQuetes.jpg'),(mainScreen.get_size()))
        self.buttonRetour = button('assets/button/retour.png', 205, 135, 105, 70)

    def update(self, mainScreen):
        mainScreen.blit(self.background, (0,0))
        mainScreen.blit(self.buttonRetour.image, self.buttonRetour.rect)