import pygame
from Projectile import projectile

class game:
    """
    Classe qui permet la gestion du fond du jeu

    ### attributs:
        - type : type du jeu
        - pressed : touches du clavier sur lesquelles l'utilisateur appuie
        - is_active : Booléen

    ### méthodes:
        - update -> met à jour la position du joueur
        - move_right -> gère le déplacement du joueur vers la droite
        - move_left -> gère le déplacement du joueur vers la gauche
        - depart_accueil -> réinitialise la position de départ du joueur ainsi que ses déplacements dès l'arrivée sur la page d'accueil
    """

    def __init__(self):
        self.type = None
        self.pressed = {}
        self.is_active = False
        self.all_projectiles = pygame.sprite.Group()
    
    def update(self, mainScreen):
        mainScreen.blit(self.type.image, self.type.pos)

    def tirer(self, pnj):
        self.all_projectiles.add(projectile(pnj))
    
    def move_right(self):
        self.type.pos.x += self.type.speed

    def move_left(self):
        self.type.pos.x -= self.type.speed

    def depart_accueil(self, mainScreen):
        self.type.pos.x = mainScreen.get_width()/2 - self.type.image.get_width()/2 # Permet de centrer l'image
        self.type.pos.y = 400
        self.pressed = {}

class guerrier(pygame.sprite.Sprite):
    """
    Classe qui permet de créer un personnage de type guerrier

    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - pos : hitbox du personnage
        - pos.x : position du personnage sur l'axe des abcisses
        - pos.y : position du personnage sur l'axe des ordonnées

    ### méthodes:
        - Pas de méthode -> Classe ne servant qu'à initialiser des personnages de la classe correspondante
    """

    def __init__(self):
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.speed = 7
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/guerrier.png"),(260,260))
        self.pos = self.image.get_rect()
        self.pos.x = 0
        self.pos.y = 0
        
    
class mage(pygame.sprite.Sprite):
    """
    Classe de gestion des caractéristiques d'un personnage type mage

    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - pos : hitbox du personnage
        - pos.x : position du personnage sur l'axe des abcisses
        - pos.y : position du personnage sur l'axe des ordonnées

    ### méthodes:
        - Pas de méthode -> Classe ne servant qu'à initialiser des personnages de la classe correspondante
    """
    def __init__(self):
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 20
        self.max_health = 20
        self.damage = 35
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/mage.png"),(260,260))
        self.pos = self.image.get_rect()
        self.pos.x = 0
        self.pos.y = 0