import pygame

class guerrier(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.speed = 5
        self.image = pygame.image.load("guerrier.png")
        self.pos = self.image.get_rect()
        self.pos.x = 400
        self.pos.y = 500

    def deplacements(self):

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.pos.x -= self.speed
                elif event.key == K_RIGHT:
                    self.pos.x += self.speed
                elif event.key == K_UP:
                    self.pos.y += self.speed
                elif event.key == K_DOWN:
                    self.pos.y -= self.speed

    
