import pygame
from Projectile import projectile
from Monster import monster

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
        self.all_player = pygame.sprite.Group()
        self.all_projectiles = pygame.sprite.Group()
        self.all_monster = pygame.sprite.Group()
    
    def update(self, mainScreen):
        mainScreen.blit(self.type.image, self.type.rect)

    def tirer(self, pnj):
        self.all_projectiles.add(projectile(pnj))
    
    def move_right(self):
        if not self.check_collision(self.type, self.all_monster):
            self.type.rect.x += self.type.speed

    def move_left(self):
        self.type.rect.x -= self.type.speed

    def depart_accueil(self, mainScreen):
        self.type.rect.x = mainScreen.get_width()/2 - self.type.image.get_width()/2 # Permet de centrer l'image
        self.type.rect.y = 425
        self.pressed = {}
    
    def spawn_monster(self, mainScreen):
        self.all_monster.add(monster(mainScreen))
        
    def check_collision(self, element, group):
        return pygame.sprite.spritecollide(element, group, False, pygame.sprite.collide_mask)

    def monster_vers_joueurs(self, mainScreen, monster, pnj, evenement, quete1, defaite, soundDesign):
        # Le déplacement ne se fait que si il n'y a pas de collision avec un monstre
        if not self.check_collision(self.type, self.all_monster):
            monster.rect.x -= monster.speed
        # Si le monstre est en collision avec le joueur:
        else:
            pnj.damage(monster, monster.attack, evenement, quete1, defaite, soundDesign)

    def update_health_bar(self, mainScreen):
        # définir une couleur et une position pour l'arrière plan de la jauge (gris foncé) et la dessiner
        pygame.draw.rect(mainScreen, (60,60,60), [self.type.rect.x + 70 ,self.type.rect.y - 30, self.type.max_health,5])
        # définir une couleur et une position pour la jauge de vie (vert) et la dessiner
        pygame.draw.rect(mainScreen, (100,200,50), [self.type.rect.x + 70 ,self.type.rect.y - 30, self.type.health,5])

    def damage(self, monster, amount, evenement, quete1, defaite, soundDesign):
        if self.type.health - amount > amount:
            self.type.health -= amount
        else:
            evenement.transit_Quete1_Defaite(self, quete1, defaite, soundDesign)
            

class guerrier(pygame.sprite.Sprite):
    """
    Classe qui permet de créer un personnage de type guerrier

    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - rect : hitbox du personnage
        - rect.x : position du personnage sur l'axe des abcisses
        - rect.y : position du personnage sur l'axe des ordonnées

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
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    
class mage(pygame.sprite.Sprite):
    """
    Classe de gestion des caractéristiques d'un personnage type mage

    ### attributs:
        - health : points de vie du personnage
        - max_health : points de vie maximum que le personnage ne peut dépasser
        - damage : points d'attaque du personnage
        - speed : vitesse du personnage
        - image : image visuelle du personnage
        - rect : hitbox du personnage
        - rect.x : position du personnage sur l'axe des abcisses
        - rect.y : position du personnage sur l'axe des ordonnées

    ### méthodes:
        - Pas de méthode -> Classe ne servant qu'à initialiser des personnages de la classe correspondante
    """
    def __init__(self):
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 100
        self.max_health = 100
        self.damage = 35
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/pnj/mage.png"),(260,260))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0