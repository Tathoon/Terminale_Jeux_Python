import pygame
import random

class monster(pygame.sprite.Sprite):
    """
    Classe qui permet la gestion des monstres

    ###attributs:
        - health : points de vie du monstre
        - max_health : points de vie maximum du monstre
        - attack : dégats du monstre
        - image : représentation iconographique
        - rect : image sous forme objet Rect
        - rect.x : coordonnées en x du monstre
        - rect.y : coordonnées en y du monstre
        - speed : vitesse de déplacement
    ###méthodes:
        - damage -> dégats reçus par le monstre
        - update_health_bar -> affiche la barre de vie des monstres actualisée à chaque dégat pris

    """
    def __init__(self, mainScreen):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/monster/mario.png"),(260,260))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(mainScreen.get_width(), mainScreen.get_width() + 400)
        self.rect.y = 425
        self.speed = random.randint(3, 7)

    def damage(self, pnj, mainScreen):
        # Infliger les dégats
        self.health -= pnj.type.damage
        if self.health <= 0:
            self.health = self.max_health
            self.rect.x = random.randint(mainScreen.get_width(), mainScreen.get_width() + 400)
            self.speed = random.randint(3, 7)

    def update_health_bar(self, mainScreen):
        # définir une couleur et une position pour l'arrière plan de la jauge (gris foncé) et la dessiner
        pygame.draw.rect(mainScreen, (60,60,60), [self.rect.x + 70 ,self.rect.y - 30,self.max_health,5])
        # définir une couleur et une position pour la jauge de vie (vert) et la dessiner
        pygame.draw.rect(mainScreen, (100,200,50), [self.rect.x + 70 ,self.rect.y - 30, self.health,5])