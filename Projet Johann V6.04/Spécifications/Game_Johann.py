import pygame

class game:
    """
    Classe qui permet la gestion du fond du jeu
    ### attributs:
        - type : type du jeu
        - pressed : touches du clavier sur lesquelles l'utilisateur appuie
        - is_active : Booléen
    ### méthodes:
        - update --> met à jour le jeu à chaque tour de boucle
        - move_right --> gère le déplacement du joueur vers la droite
        - move_left --> gère le déplacement du joueur vers la gauche
        - depart_accueil --> réinitialise la position de départ du joueur ainsi que ses déplacements dès l'arrivée sur la page d'accueil
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
    Classe qui permet de créer un personnage de type guerrier
    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - pos : hitbox du personnage
        - posx : position du personnage sur l'axe des abcisses
        - posy : position du personnage sur l'axe des ordonnées

    ### méthodes:
        - Pas de méthode --> Classe ne servant qu'à initialiser des personnages de la classe correspondante
    """

    def __init__(self):

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
    Classe qui permet de créer un personnage de type mage
    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - pos : hitbox du personnage
        - posx : position du personnage sur l'axe des abcisses
        - posy : position du personnage sur l'axe des ordonnées

    ### méthodes:
        - Pas de méthode --> Classe ne servant qu'à initialiser des personnages de la classe correspondante
    """

    def __init__(self):

        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 20
        self.max_health = 20
        self.damage = 35
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/mage.png"),(330,330))
        self.pos = self.image.get_rect()
        self.pos.x = 400
        self.pos.y = 330
