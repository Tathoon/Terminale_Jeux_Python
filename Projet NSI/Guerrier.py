import pygame

class guerrier(pygame.sprite.Sprite):

    def __init__(self):
        """ le constructeur initialise le personnage selon un certain nombre de points de vie,
            de dégats infligés, sa vitesse de déplacement, ainsi que sa position initiale
            les attributs health, max_health, damage, speed, pos.x et pos.y dont de type int
        """
        super().__init__() #on fait appel à la super classe sprite de pygame
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.speed = 5
        self.image = pygame.image.load("guerrier.png")
        self.pos = self.image.get_rect()
        self.pos.x = 400
        self.pos.y = 500


    def deplacements(self):
        """ méthode de la classe guerrier permettant de déplacer le personnage 
            en fonction de la touche sur laquelle on reste appuyée
        """ 
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if guerrier.pressed.get(pygame.K_LEFT):
                    self.pos.x -= self.speed
                elif guerrier.pressed.get(pygame.K_RIGHT):
                    self.pos.x += self.speed
                elif guerrier.pressed.get(pygame.K_UP):
                    self.pos.y -= self.speed
                elif guerrier.pressed.get(pygame.K_DOWN):
                    self.pos.y += self.speed

