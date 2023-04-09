import pygame

class projectile(pygame.sprite.Sprite):

    def __init__(self, pnj):
        super().__init__()
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("assets/projectile/bombe.png"),(85,85))
        self.rect = self.image.get_rect()
        self.rect.x = pnj.type.pos.x + 120
        self.rect.y = pnj.type.pos.y + 120
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) # considère l'image par son centre pour une rotation plus réaliste

    def remove(self, pnj):
        pnj.all_projectiles.remove(self)

    def move(self, mainScreen, pnj):
        self.rect.x += self.speed
        self.rotate()

        if self.rect.x > mainScreen.get_width():
            self.remove(pnj)
            