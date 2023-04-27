import pygame

class game:
    """
    Classe qui permet

    ### attributs:
        - bla : blala

    ### méthodes:
        - bla -> blabla
    """

    def __init__(self):
        self.type = None
        self.pressed = {}
        self.is_active = False
    
    def update(self, mainScreen):
        mainScreen.blit(self.type.image, self.type.pos)
    
    def move_right(self):
        self.type.pos.x += self.type.speed

    def move_left(self):
        self.type.pos.x -= self.type.speed

    def depart_accueil(self):
        self.type.pos.x = 400
        self.type.pos.y = 330
        self.pressed = {}

class guerrier(pygame.sprite.Sprite):
    """
    Classe qui permet

    ### attributs:
        - bla : blala

    ### méthodes:
        - bla -> blabla
    """

    def __init__(self):
        """ le constructeur initialise le personnage selon un certain nombre de points de vie,
            de dégats infligés, sa vitesse de déplacement, ainsi que sa position initiale
            les attributs health, max_health, damage, speed, pos.x et pos.y dont de type int
        """
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.speed = 7
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/guerrier.png"),(330,330))
        self.pos = self.image.get_rect()
        self.pos.x = 400
        self.pos.y = 330
        
    
class mage(pygame.sprite.Sprite):
    """
    Classe de gestion des caractéristiques d'un personnage type mage
    """

    def __init__(self):
        """ le constructeur initialise le personnage selon un certain nombre de points de vie,
            de dégats infligés, sa vitesse de déplacement, ainsi que sa position initiale
            les attributs health, max_health, damage, speed, pos.x et pos.y dont de type int
        """
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 20
        self.max_health = 20
        self.damage = 35
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/mage.png"),(330,330))
        self.pos = self.image.get_rect()
        self.pos.x = 400
        self.pos.y = 330